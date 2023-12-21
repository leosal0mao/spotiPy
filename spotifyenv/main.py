import sys

sys.path.append("spotifyenv/spotify_calls")
sys.path.append("spotifyenv/youtube_calls")

from spotify_search import *
from search_youtube_videos import *
from generate_video_link import *

# get_spotify_playlist_songs("spotify:playlist:5X3IDSizPjZKIt5j1uerIj")

# video_id = search_videos_and_return_id("slowdive alife")

# video_link = generate_video_link(video_id)
# print(video_link)
# search_youtube_videos("alife slowdive")
