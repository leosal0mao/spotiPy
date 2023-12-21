import spotipy
import os

from required_keys import *
from spotipy.oauth2 import SpotifyClientCredentials


##Client credentials(public and secret keys, see documentation on how to set it up)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def get_spotify_playlist_songs(playlist_url):
    
    playlist_info = spotify.playlist_items(
    playlist_id=playlist_url,
    fields="items",
    )
    
    playlist_tracks = playlist_info["items"]

    track_list = []
    for track_info in playlist_tracks:
        track = f'{track_info["track"]["name"]} - {track_info["track"]["artists"][0]['name']}'
        track_list.append(track)
        
    ##remove any old tracks.txt file for a better performance and cleaner environment
    if os.path.exists('tracks.txt'):
        os.remove('tracks.txt')
    else: 
        pass

    with open(r'tracks.txt', 'w') as fp:   
        fp.write('\n'.join(str(track) for track in track_list))


    

