# flvto
Made for beatmakers who need to bulk download a lot of .mp3s at once.

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [USAGE](#usage)
- [CONFIGURATION](#configuration)

# INSTALLATION

You will need [Python 3,](https://www.python.org/downloads/) [youtube-dl,](https://ytdl-org.github.io/youtube-dl/download.html) and [ffmpeg.](https://ffmpeg.zeranoe.com/builds/)

If you are on windows, the youtube-dl download also includes Python. Place it in any location on your [PATH](https://en.wikipedia.org/wiki/PATH_%28variable%29) except for `%SYSTEMROOT%\System32` (e.g. **do not** put in `C:\Windows\System32`).

# DESCRIPTION

**flvto** is a command-line program to extract audio from YouTube videos as 256kbps .mp3 files. It requires the Python 3 interpreter, and currently works solely on Windows. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

    λ flvto 
    flvto version 3.2
    Enter a list of videos to convert (ENTER when done):
    > https://www.youtube.com/watch?v=CRnaiUEPBuQ
    > https://www.youtube.com/watch?v=ifJdXauIH28
    > 
    
    [flvto] Working . . .
    [flvto] 1/2 samples processed . . . [00:15]
    [flvto] 2/2 samples processed . . . [00:21]
    
    2 samples saved to samples/9-21-2019 [00:36]
    
# USAGE

Simply run the `flvto.exe` in the `dist` folder. 

You can also run it by calling `λ python flvto.py`.

If you want to be able to run it from the terminal, add `flvto\dist\` to your [path.](https://en.wikipedia.org/wiki/PATH_%28variable%29)

# CONFIGURATION

You can change the directory you wish to save your samples to by editing `%APPDATA%/flvto/path.txt`. This will read as `C:\Users\name\AppData\Roaming\flvto\path.txt`. Alternatively, you can just delete it, and the program will prompt you to enter a new one when you run it again.
