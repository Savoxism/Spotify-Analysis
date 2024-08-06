import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def get_token():
    auth_response = requests.post('https://accounts.spotify.com/api/token', 
                                      auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
                                  data={'grant_type': 'client_credentials'})
    return auth_response.json()['access_token']

def get_artist_info(uri, token):
    artist_id = uri.split(':')[-1]
    response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}', 
                            headers={'Authorization': f'Bearer {token}'})
    return response.json()['name'] if response.status_code == 200 else None

def get_track_info(uri, token):
    track_id = uri.split(':')[-1]
    response = requests.get(f'https://api.spotify.com/v1/tracks/{track_id}', 
                            headers={'Authorization': f'Bearer {token}'})
    if response.status_code == 200:
        track_data = response.json()
        return {
            'name': track_data['name'],
            'artist': track_data['artists'][0]['name'],
            'album': track_data['album']['name']
        }
    else:
        return None
      
# Get Top Artists Info
# with open('datasets/top_5_artists.json', 'r') as f:
#         top_5_uris = json.load(f)
        
# token = get_token()
# for uri in top_5_uris:
#         name = get_artist_info(uri, token)
#         print(f"{uri}: {name}")

###################################
# Get Top Tracks Info
# with open('datasets/top_tracks_uris.json', 'r') as f:
#         track_uris = json.load(f)

# token = get_token()
# for uri in track_uris:
#     track_info = get_track_info(uri, token)
#     if track_info:
#         print(f"{uri}:")
#         print(f"  Track: {track_info['name']}")
#         print(f"  Artist: {track_info['artist']}")
#         print(f"  Album: {track_info['album']}")
#         print()
#     else:
#         print(f"Could not fetch info for {uri}")