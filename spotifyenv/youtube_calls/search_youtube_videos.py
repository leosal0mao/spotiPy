from required_keys import *
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build


def search_videos_and_return_id(query):
    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_KEY,
    )
    try:
        request = youtube.search().list(part="id", type="video", q=query, maxResults=5)
        response = request.execute()

        videoid = response["items"][0]["id"]["videoId"]

        return videoid
    except HttpError as e:
        print(f"An error occurred: {e}")
        return None
