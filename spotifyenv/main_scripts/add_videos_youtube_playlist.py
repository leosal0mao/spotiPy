import sys
import os

sys.path.append("spotifyenv/spotify_calls")
sys.path.append("spotifyenv/youtube_calls")
sys.path.append("spotifyenv")

from spotify_search import *
from search_youtube_videos import *
from generate_video_link import *
from create_add_video_to_playlist import *


def add_videos_to_youtube_playlist():
    # clean console in all OS
    os.system("cls")
    os.system("clear")

    spotifyPlaylistLink = input("Enter your playlist link: ")
    get_spotify_playlist_songs(spotifyPlaylistLink)

    youtubePlaylistName = input("enter a name for your playlist: ")
    youtubePlaylistId = create_youtube_playlist_and_id(youtubePlaylistName)

    # open youtube_videos_ids file and get all video_ids to insert into the newly created playlist
    with open("youtube_videos_ids.txt", "r") as file:
        video_id_list = file.readlines()

    video_id_list = [line.strip() for line in video_id_list]

    for video_id in video_id_list:
        add_video_to_playlist(video_id, youtubePlaylistId)
