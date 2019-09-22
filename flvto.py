#!/usr/bin/env python3

import os
import subprocess

from datetime import date, datetime
from time import sleep


def get_path():
    """creates the path file used to store what directory to save samples in
    if not already made. otherwise, reads and returns path string from path.txt
    """
    if not os.path.exists(f"{os.getenv('APPDATA')}\\flvto\\path.txt"):
        try:
            os.mkdir(f"{os.getenv('APPDATA')}\\flvto")
        except FileExistsError:
            pass    # if the folder already exists, just make the file

        print("Enter the directory to save samples to:")
        print("[example] > C:\\Users\\name\\samples")
        path = input("> ")

        with open(f"{os.getenv('APPDATA')}\\flvto\\path.txt", "w") as f:
            f.write(path)
        print("Bet\n")
    else:
        with open(f"{os.getenv('APPDATA')}\\flvto\\path.txt", "r") as f:
            path = f.readline()

    return path


def main():
    print("flvto version 3.2")

    videos = []
    url = ""
    # folder naming format is /samples/month-day-year
    # e.g. /samples/9-21-2019
    dirname = f"{date.today().month}-{date.today().day}-{date.today().year}"
    path = get_path() + "\\"
    runtime = 0

    # read in a stream of videos
    print("Enter a list of videos to convert (ENTER when done):")
    url = input("> ")
    while url != "":
        videos.append(url)
        url = input("> ")

    try:
        os.mkdir(f"{path}{dirname}")
    except FileExistsError:  # user has downloaded samples earlier today
        pass

    print("\n[flvto] Working . . .")  # flavor text
    for n, video in enumerate(videos, 1):
        start = datetime.now()  # keep track of how long each video takes
        # runs youtube-dl to download audio, uses ffmpeg to convert to mp3,
        # and saves each video in the aforementioned directory
        subprocess.run(["youtube-dl", video, "-x", "--audio-format",
                        "mp3", "--audio-quality", "0", "-o",
                        f"{path}{dirname}/%(title)s.%(ext)s", "-q"])

        time = (datetime.now() - start).total_seconds()
        print(f"[flvto] {n}/{len(videos)} samples processed . . .", end=" ")
        # formats time as [mm:ss] e.g. [01:24]
        print(f"[{int(time//60):0>2d}:{int(time%60):0>2d}]")
        runtime += time

    # prints 'sample' if only 1 video, 'samples' if multiple
    print(f"\n{len(videos)} sample{'' if len(videos) == 1 else 's'} " +
          f"saved to {dirname}", end=" ")
    print(f"[{int(runtime//60):0>2d}:{int(runtime%60):0>2d}]")

    # opens the directory we just saved the videos to in file explorer
    print("Opening folder . . .")
    subprocess.run(["explorer", f"{path}{dirname}"])
    sleep(10)  # so the window doesn't close immediately


if __name__ == '__main__':
    main()
