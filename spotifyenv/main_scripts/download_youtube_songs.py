import os
import glob

from pydub import AudioSegment
from pathlib import Path
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_youtube_songs(url):
    try:
        ytb = YouTube(url)
    except VideoUnavailable:
        print(f"Video {ytb.title} is unavailable, skipping.")
    else:
        path_to_download_pc = str(os.path.join(Path.home(), "Downloads/pysongs"))
        extension_list = ("*.webm", "*.mp4")

        print(f"Downloading video: {ytb.title}")

        ytb.streams.filter(
            only_audio=True,
            abr="160kbps",
        ).first().download(path_to_download_pc)

        os.chdir(path_to_download_pc)
        for extension in extension_list:
            for video in glob.glob(extension):
                mp3_filename = os.path.splitext(os.path.basename(video))[0] + ".mp3"
                AudioSegment.from_file(video).export(mp3_filename, format="mp3")

    for webmpath in glob.iglob(os.path.join(path_to_download_pc, "*.webm")):
        os.remove(webmpath)
    # for item in webm_deletion_path:
    #     if item.endswith(".webm"):
    #         os.remove(os.path.join(webm_deletion_path, item))
