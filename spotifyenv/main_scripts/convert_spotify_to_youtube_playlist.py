# this file transforms the tracks from spotify conversion into a youtube list with links

import sys
import os

sys.path.append("spotifyenv/youtube_calls")
sys.path.append("spotifyenv")

from required_keys import *
from search_youtube_videos import *
from generate_video_link import *


def convert_spotify_to_youtube_txt():
    with open("spotify_tracks.txt", "r") as file:
        track_list = file.readlines()

    track_list = [line.strip() for line in track_list]

    youtube_links = []
    youtube_video_ids = []
    for track in track_list:
        video_link = generate_video_link(search_videos_and_return_id(track))
        video_id = search_videos_and_return_id(track)
        youtube_links.append(video_link)
        youtube_video_ids.append(video_id)

    ##remove any old youtube_links.txt file for a better performance and cleaner environment
    if os.path.exists("youtube_links.txt"):
        os.remove("youtube_links.txt")
        os.remove("youtube_videos_ids.txt")
    else:
        pass

    with open(r"youtube_links.txt", "w") as fp:
        fp.write("\n".join(str(video_link) for video_link in youtube_links))
    with open(r"youtube_videos_ids.txt", "w") as fp:
        fp.write("\n".join(str(video_id) for video_id in youtube_video_ids))
