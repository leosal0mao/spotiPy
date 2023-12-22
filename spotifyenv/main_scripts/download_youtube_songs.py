import os

from pathlib import Path
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_youtube_songs(url):
    try:
        ytb = YouTube(url)
    except VideoUnavailable:
        print(f"Video {ytb.title} is unavailable, skipping.")
    else:
        print(f"Downloading video: {ytb.title}")
        path_to_download = str(os.path.join(Path.home(), "Downloads/pysongs"))

        ytb.streams.filter(
            only_audio=True,
            abr="160kbps",
        ).first().download(
            path_to_download,
        )
