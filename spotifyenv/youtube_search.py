import os
import flask
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from required_keys import *
from googleapiclient.discovery import build


def search_videos(query):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
    )
    request = youtube.search().list(part="id", type="video", q=query, maxResults=5)
    response = request.execute()

    return response


query = "Eternal Rest - Sidewalks and Skeletons"
results = search_videos(query)
print(results)


def add_video_to_playlist(video_id, playlist_id):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
    )
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {"kind": "youtube#video", "videoId": video_id},
            }
        },
    )
    response = request.execute()
    return response


def create_youtube_playlist(playlist_name):
    youtube = build(
        "youtube", "v3", developerKey="AIzaSyAKupMVv6GE6Mj9wlBudlHSgcIQXzYIG6Y"
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
    return response


# playlist = create_youtube_playlist("teste")
# print(playlist)


# Use the client_secret.json file to identify the application requesting
# authorization. The client ID (from that file) and access scopes are required.
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    "spotifyenv/client_secret.json",
    scopes=["https://www.googleapis.com/auth/youtube.force-ssl"],
)

# Indicate where the API server will redirect the user after the user completes
# the authorization flow. The redirect URI is required. The value must exactly
# match one of the authorized redirect URIs for the OAuth 2.0 client, which you
# configured in the API Console. If this value doesn't match an authorized URI,
# you will get a 'redirect_uri_mismatch' error.
flow.redirect_uri = "https://www.example.com/oauth2callback"

# Generate URL for request to Google's OAuth 2.0 server.
# Use kwargs to set optional request parameters.
authorization_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type="offline",
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes="true",
)
