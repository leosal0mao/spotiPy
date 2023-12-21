import sys

sys.path.append("spotifyenv")
sys.path.append("spotifyenv/youtube_calls")

from required_keys import *
from youtube_authentication import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials = get_existing_credentials()


def create_youtube_playlist_and_id(playlist_name):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
        credentials=credentials,
    )
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


def add_video_to_playlist(video_id, playlist_id):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
        credentials=credentials,
    )
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
    return response
