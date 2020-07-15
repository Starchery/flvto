#!/usr/bin/env python3

import concurrent.futures as cf
from threading import Thread
import os
import sys
import youtube_dl
import time
import getpass
from abc import ABC, abstractmethod
from collections import deque
from datetime import date 
from enum import Enum, auto, unique
from functools import partial, wraps
from typing import *
from pathlib import Path


import platform

if platform.system() == 'Windows':
    try:
        import colorama
    except ImportError:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        # Enable ANSI support on Windows 10 v1511
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    else:
        colorama.init()
else:
    # Fix Linux arrow key support in Python scripts
    import readline


class TempHistory:
    """Record one line from the terminal.

    It is necessary to keep track of the last line on the terminal so we
    can move the text cursor rightward and upward back into the position
    before the newline from the `input` function was echoed.

    Note: I use the term 'echo' to refer to when text is
    shown on the terminal but might not be written to `sys.stdout`.

    """

    def __init__(self):
        """Initialise `line` and save the `print` and `input` functions.

        `line` is initially set to '\n' so that the `record` method
        doesn't raise an error about the string index being out of range.

        """
        self.line = '\n'
        self.builtin_print = print
        self.builtin_input = input

    def _record(self, text):
        """Append to `line` or overwrite it if it has ended."""
        if text == '':
            # You can't record nothing
            return
        # Take into account `text` being multiple lines
        lines = text.split('\n')
        if text[-1] == '\n':
            last_line = lines[-2] + '\n'
            # If `text` ended with a newline, then `text.split('\n')[-1]`
            # would have merely returned the newline, and not the text
            # preceding it
        else:
            last_line = lines[-1]
        # Take into account return characters which overwrite the line
        last_line = last_line.split('\r')[-1]
        # `line` is considered ended if it ends with a newline character
        if self.line[-1] == '\n':
            self.line = last_line
        else:
            self.line += last_line

    def _undo_newline(self):
        """Move text cursor back to its position before echoing newline.

        ANSI escape sequence: `\x1b[{count}{command}`
        `\x1b` is the escape code, and commands `A`, `B`, `C` and `D` are
        for moving the text cursor up, down, forward and backward {count}
        times respectively.

        Thus, after having echoed a newline, the final statement tells
        the terminal to move the text cursor forward to be inline with
        the end of the previous line, and then move up into said line
        (making it the current line again).

        """
        line_length = len(self.line)
        # Take into account (multiple) backspaces which would
        # otherwise artificially increase `line_length`
        for i, char in enumerate(self.line[1:]):
            if char == '\b' and self.line[i-1] != '\b':
                line_length -= 2
        self.print('\x1b[{}C\x1b[1A'.format(line_length),
                   end='', flush=True, record=False)

    def print(self, *args, sep=' ', end='\n', file=sys.stdout, flush=False,
              record=True):
        """Print to `file` and record the printed text.

        Other than recording the printed text, it behaves exactly like
        the built-in `print` function.

        """
        self.builtin_print(*args, sep=sep, end=end, file=file, flush=flush)
        if record:
            text = sep.join([str(arg) for arg in args]) + end
            self._record(text)

    def input(self, prompt='', newline=True, record=True):
        """Return one line of user input and record the echoed text.

        Other than storing the echoed text and optionally stripping the
        echoed newline, it behaves exactly like the built-in `input`
        function.

        """
        if prompt == '':
            # Prevent arrow key overwriting previously printed text by
            # ensuring the built-in `input` function's `prompt` argument
            # isn't empty
            prompt = ' \b'
        try:
            response = self.builtin_input(prompt)
        except EOFError:
            sys.exit(1)
        if record:
            self._record(prompt)
            self._record(response)
        if not newline:
            self._undo_newline()
        return response


def timer(func):
    @wraps(func)
    def wrapper_timer(*args):
        start_time = time.perf_counter()    # 1
        value = func(*args)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


class Video:
    def __init__(self, url: str, ydl):
        self.url = url
        try:
            info = ydl.extract_info(self.url, download=False)
            self.name = info.get("title", None)
        except Exception as e:
            raise e

    def download(self, ydl) -> int:
        try:
            return ydl.download([self.url])
        except Exception:
            pass


class DummyLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass


class VideoLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    @staticmethod
    def error(msg, offender):
        offender = msg[msg.find("'")+1:msg.find("'", msg.find("'") + 1)]
        if platform.system() == "Windows":
            cols = int(os.popen("MODE", "r").read().split()[8])
        else:
            cols = os.popen('stty size', 'r').read().split()[1]

        log_msg = "[flvto log] "
        if "not a valid URL." in msg:
            log_msg += f"{msg[:msg.find('.') + 1]}"
        else:
            log_msg += "ERROR: "
            log_msg += msg[msg.find("'")+1:msg.find("'", msg.find("'") + 1)]
        prompt = f"\r> {offender}"
        print(f"{prompt}{' '*(cols-(len(log_msg) + len(prompt)))}{log_msg}")
        # print(msg, offender)


class VideoMonitor:
    def __init__(self, path):
        self.complete = False
        self.path = path
        self.finished = []
        self.tasks = []
        self.worker = Thread(target=self.monitor, daemon=True)
        self.videos = deque()

    def monitor(self):
        while True:
            if len(self.videos) > 0:
                if len(self.finished) > 0:
                    time.sleep(0.3)
                    vid = self.path / self.finished.pop()
                    while len(list(vid.parent.glob(f"{vid.name}.*"))) > 1:
                        if self.complete:
                            print(" \r",end="")
                        time.sleep(0.5)
                    self.tasks.remove(vid.name[0].upper())
                    self.tasks.insert(0, "✔")
                    url = self.videos.popleft()
                    # if not self.complete:
                    print(f"\r> ", end="")
                    print(f"{' ' * (44 - 0)}{self.current_tasks()}\r> ", end="")
                    # else:
                    #     print(f"{' ' * (44 - 0)}{self.current_tasks()}\r")
                    time.sleep(0.5)
            time.sleep(0.5)
                                                                                                                                                    
    def error(self, e, offender):
        msg = e.__str__()
        prompt = "> "
        if platform.system() == "Windows":
            cols = int(os.popen("MODE", "r").read().split()[8])
        else:
            cols = int(os.popen('stty size', 'r').read().split()[1])

        log_msg = f"[flvto log] ERROR: '{offender}' is not a valid URL."
        # if "not a valid URL." in msg:
        #     log_msg += f"{msg[:msg.find('URL') + 4]}"
        # else:
        #     log_msg += f"'{offender}' is not a valid URL."
        total = len(offender) + len(log_msg) + 2
        # print(total,len(log_msg),sep='\n')

        if len(prompt) + len(offender) + len(log_msg) > cols:
            if (len(offender) + len(log_msg)) > (cols - len(prompt)):
                offender = offender[:max((cols-len(prompt))-len(log_msg), 0)]
            if len(log_msg) > (cols-len(prompt)):
                # log_msg = log_msg[:(cols-len(prompt))]
                x = log_msg.split("'")
                x[1] = x[1][:cols - (len(x[0]) + len(x[2]))-7]
                x[1] += "..." 
                log_msg = "'".join(x)

        
        if len(offender) > 0:
            spacing = " " * ((cols-len(prompt)) - ((len(offender) + len(log_msg))))
        else:
            spacing = ""
        print(f"\r{prompt}{offender}{spacing}{log_msg}")
    
    def current_tasks(self):
        return '[' + ", ".join(self.tasks) + ']'


# TODO: Implement better progress hook, command line args,
# TODO: Test on linux, refine timing system
class VideoDownloader:
    def __init__(self, path: Path, *videos):
        self.videos: Deque[Video] = deque()
        self.path = path
        self.args: Dict[str, Any] = {
            'format': 'bestaudio/best',
            'restrictfilenames': True,
            'outtmpl': f"{str(path)}/%(title)s.%(ext)s",
            'logger': DummyLogger(),
            'progress_hooks': [self.progress_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        self.downloader = youtube_dl.YoutubeDL(self.args)
        self.queue = cf.ThreadPoolExecutor()
        self.results = { }
        self.current_tasks = list()
        self.monitor = VideoMonitor(self.path)
        self.monitor.worker.start()
    
    def load(self, video: Video):
        if not video:
            self.analyze()
            self.monitor.complete = True
        else:
            self.videos.append(video)
            self.monitor.videos.append(video.url)
            result = self.start()
            self.results[result] = video.url
            self.monitor.tasks.append(video.name[0].upper())
    
    def start(self):
        download = lambda vid: vid.download(self.downloader)
        return self.queue.submit(download, self.videos.popleft())
    
    def analyze(self) -> bool:
        for value in cf.as_completed(self.results):
            try:
                data = value.result()
            except Exception as e:
                print(f"[flvto] {self.results[value]}: {e}")
                return False
        return True
    
    def progress_hook(self, download):
        title: str = Path(download['filename']).name[:-4]
        if download["status"] == "error":
            print(f"[flvto] Error processing video")
        elif download['status'] == "downloading":
            pass
            # sys.stdout.write(f"\r[flvto] Downloading {title}...\r")
            # sys.stdout.flush()
        elif download["status"] == "finished":
            # print("CVERTI")
            name = download["filename"][::-1]
            name = name[name.find(".") + 1:][::-1]
            self.monitor.finished.append(name)
            # print(f"CONVERTING {title} :)")
            # self.current_tasks.remove(title[0].upper())
            # sys.stdout.write(f"\r[flvto] Converting {title}...\r")
            # sys.stdout.flush()

    # def monitor(self):
    #     while not self.complete:
    #         if self.finished:
    #             vid = self.path / self.finished.pop()
    #             while len(list(vid.glob(f"{vid.name}.*"))) > 1:
    #                 time.sleep(1)
    #             self.current_tasks.remove(vid.name[0].upper())

    def tasks(self):
        # return '[' + ", ".join(self.monitor.tasks) + ']'
        return self.monitor.current_tasks()


class App:
    def __init__(self, version: str):
        print(f"flvto version {version}")
        self.datestring = f"{date.today().isoformat()}"
        self.cfg_path = Path.home().expanduser().resolve() / ".flvto/path.txt"
        self.record = TempHistory()
        self.print = self.record.print
        self.input = self.record.input

    def start(self):
        self.dl_folder: Path = self.read_dir_from_cfg(self.cfg_path)
        self.dl_folder = self.dl_folder / self.datestring

        downloader: VideoDownloader = VideoDownloader(self.dl_folder)

        runtime: float = time.monotonic()
        self.load_videos(downloader)
        runtime = time.monotonic() - runtime
        print(f"Total runtime: {runtime:.2f}s")

    def read_dir_from_cfg(self, cfg: Path) -> Path:
        if cfg.exists():
            dl_path = Path(cfg.read_text()).expanduser().resolve()
            if not dl_path.exists():
                dl_path.mkdir(parents=True)
            return dl_path
        else:
            try:
                cfg.touch()
            except FileNotFoundError:
                cfg.parent.mkdir(parents=True)
                cfg.touch()
            finally:
                dl_path = Path(self.query_path()).expanduser().resolve()
                cfg.write_text(str(dl_path) + '\n')
                a = Path()
                return dl_path

    def query_path(self) -> Path:
        print("Enter the directory to save samples to:")
        print("[example] > C:\\Users\\name\\samples")

        new_path: Path = Path(input("> ")).expanduser().resolve()
        if not new_path.exists():
            new_path.mkdir(parents=True)
        return new_path

    # @timer
    def load_videos(self, vdl: VideoDownloader) -> None:
        print("Enter a list of videos to convert", end=" ")
        print("(ENTER a blank entry when done):")

        for i in range(1, 10000):
            # self.print("> ", end="", flush=True)
            url: str = self.input("> ", newline=False)
            sys.stdout.flush()
            if url == "":
                break

            try:
                vdl.load(Video(url, vdl.downloader))
                print(f"\r> {url}{' ' * (44 - len(url))}{vdl.tasks()}")
            except Exception as e:
                vdl.monitor.error(e, url)
        sys.stdout.flush()
        vdl.load(None)
        print("\r")

    def kill(self):
        if os.name == "nt":
            print("Opening download folder...")
            os.startfile(os.path.normpath(self.dl_folder), "explore")
        sys.exit(0)


def main() -> None:
    flvto = App(version="4.0")
    flvto.start()
    flvto.kill()


if __name__ == '__main__':
    main()
