import sys
import os

sys.path.append("spotifyenv/spotify_calls")
sys.path.append("spotifyenv/youtube_calls")
sys.path.append("spotifyenv/main_scripts")
sys.path.append("spotifyenv")

from spotify_search import *
from download_youtube_songs import *
from convert_spotify_to_youtube_playlist import *

# clean console in all OS
os.system("cls")
os.system("clear")


spotifyPlaylistLink = input("Enter your playlist link: ")
get_spotify_playlist_songs(spotifyPlaylistLink)

convert_spotify_to_youtube_txt()

with open("youtube_links.txt", "r") as file:
    links = file.readlines()

link_list = [line.strip() for line in links]

for link in link_list:
    download_youtube_songs(link)
