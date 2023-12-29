import sys

sys.path.append("spotifyenv")
sys.path.append("spotifyenv/youtube_calls")

from required_keys import *
from youtube_authentication import *
from googleapiclient.discovery import build

credentials = get_existing_credentials()


def create_youtube_playlist_and_id(playlist_name):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
        credentials=credentials,
    )
    try:
        request = youtube.playlists().insert(
            part="snippet",
            body={
                "snippet": {
                    "title": playlist_name,
                }
            },
        )
        response = request.execute()
        playlistId = response["id"]

        return playlistId
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def add_video_to_playlist(video_id, playlist_id):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
        credentials=credentials,
    )
    try:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id,
                    },
                }
            },
        )
        response = request.execute()
        playlistItemId = response["id"]

        return playlistItemId
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
