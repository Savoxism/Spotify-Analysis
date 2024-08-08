import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')


# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_features(track_id):
    features = sp.audio_features(track_id)[0]
    
    relevant_features = {
        'danceability': features['danceability'],
        'energy': features['energy'],
        'key': features['key'],
        'loudness': features['loudness'],
        'mode': features['mode'],
        'speechiness': features['speechiness'],
        'acousticness': features['acousticness'],
        'instrumentalness': features['instrumentalness'],
        'liveness': features['liveness'],
        'valence': features['valence'],
        'tempo': features['tempo']
    }
    
    return relevant_features

def get_track_info(track_id):
    track_info = sp.track(track_id)
    return {
        'name': track_info['name'],
        'artist': track_info['artists'][0]['name'],
        'album': track_info['album']['name'],
        'release_date': track_info['album']['release_date']
    }


track_id = '6sLr2dwt4DdlcupzKFZVrP'  

# Get track info and features
# track_info = get_track_info(track_id)
track_features = get_track_features(track_id) 

# Combine info and features
track_data = {**track_features}

df = pd.DataFrame([track_data])

print(df)

