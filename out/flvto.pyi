from typing import *
from enum import Enum as Enum, auto as auto, unique as unique
from functools import partial as partial
from pathlib import Path
from typing import Any

kernel32: Any

class TempHistory:
    line: str = ...
    builtin_print: Any = ...
    builtin_input: Any = ...
    def __init__(self) -> None: ...
    def print(self, *args: Any, sep: str = ..., end: str = ..., file: Any = ..., flush: bool = ..., record: bool = ...) -> None: ...
    def input(self, prompt: str = ..., newline: bool = ..., record: bool = ...): ...

def timer(func: Any): ...

class Video:
    url: Any = ...
    name: Any = ...
    def __init__(self, url: str, ydl: Any) -> None: ...
    def download(self, ydl: Any) -> int: ...

class DummyLogger:
    def debug(self, msg: Any) -> None: ...
    def warning(self, msg: Any) -> None: ...
    def error(self, msg: Any) -> None: ...

class VideoLogger:
    def debug(self, msg: Any) -> None: ...
    def warning(self, msg: Any) -> None: ...
    @staticmethod
    def error(msg: Any, offender: Any) -> None: ...

class VideoMonitor:
    complete: bool = ...
    path: Any = ...
    finished: Any = ...
    tasks: Any = ...
    worker: Any = ...
    videos: Any = ...
    def __init__(self, path: Any) -> None: ...
    def monitor(self) -> None: ...
    def error(self, e: Any, offender: Any) -> None: ...
    def current_tasks(self): ...

class VideoDownloader:
    videos: Any = ...
    path: Any = ...
    args: Any = ...
    downloader: Any = ...
    queue: Any = ...
    results: Any = ...
    current_tasks: Any = ...
    monitor: Any = ...
    def __init__(self, path: Path, *videos: Any) -> None: ...
    def load(self, video: Video) -> Any: ...
    def start(self): ...
    def analyze(self) -> bool: ...
    def progress_hook(self, download: Any) -> None: ...
    def tasks(self): ...

class App:
    datestring: Any = ...
    cfg_path: Any = ...
    record: Any = ...
    print: Any = ...
    input: Any = ...
    def __init__(self, version: str) -> None: ...
    dl_folder: Any = ...
    def start(self) -> None: ...
    def read_dir_from_cfg(self, cfg: Path) -> Path: ...
    def query_path(self) -> Path: ...
    def load_videos(self, vdl: VideoDownloader) -> None: ...
    def kill(self) -> None: ...

def main() -> None: ...
