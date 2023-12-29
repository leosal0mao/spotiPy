import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
SECRETS = "spotifyenv/client_secret.json"


def get_authenticated_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds.valid:
        try:
            flow = InstalledAppFlow.from_client_secrets_file(SECRETS, SCOPES)
            creds = flow.run_local_server(port=8000)
            # Save the credentials for the next run
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        except HttpError as e:
            creds = None
            raise Exception(f"An error occurred: {e}, no credentials provided")

    return build("youtube", "v3", credentials=creds)


def get_existing_credentials():
    # If the token.pickle file exists, use the credentials from it
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            credentials = pickle.load(token)

        # If the credentials are not valid, get the authenticated service
        if not credentials.valid:
            get_authenticated_service()
            get_existing_credentials()

    return credentials
