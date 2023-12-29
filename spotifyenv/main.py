import sys

sys.path.append("spotifyenv/main_scripts")

from main_scripts.add_videos_youtube_playlist import *
from main_scripts.download_videolist_script import *

print("What you want to do?")
print("1.Convert spotify playlist to youtube playlist")
print("2.Convert spotify playlist to mp3")
print("-----------------")

inputNumber = input("Choose an option: ")

match inputNumber:
    case "1":
        add_videos_to_youtube_playlist()
    case "2":
        download_mp3_playlist()
    case _:
        print("Invalid Option! Choose another.")
