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
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

        # If the credentials are not valid, get the authenticated service
        if not creds.valid:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(SECRETS, SCOPES)
                creds = flow.run_local_server(port=8000)
                # Save the credentials for the next run
                with open("token.pickle", "wb") as token:
                    pickle.dump(creds, token)
            except HttpError as e:
                creds = None
                raise Exception(f"No credentials provided {e}")

    else:
        try:
            flow = InstalledAppFlow.from_client_secrets_file(SECRETS, SCOPES)
            creds = flow.run_local_server(port=8000)
            # Save the credentials for the next run
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)
        except HttpError as e:
            creds = None
            raise Exception(f"No credentials provided {e}")

    return creds
