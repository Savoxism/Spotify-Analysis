import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify API credentials
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_track_features(track_id):
    """
    Extracts audio features for a given Spotify track ID.
    """
    # Get track audio features
    features = sp.audio_features(track_id)[0]
    
    # Extract specific features
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
    """
    Retrieves basic information about a track.
    """
    track_info = sp.track(track_id)
    return {
        'name': track_info['name'],
        'artist': track_info['artists'][0]['name'],
        'album': track_info['album']['name'],
        'release_date': track_info['album']['release_date']
    }

# Example usage
track_id = '1l5OmUzVCkZlvrCYTFwrq3'  

# Get track info and features
# track_info = get_track_info(track_id)
track_features = get_track_features(track_id) 

# Combine info and features
track_data = {**track_features}

# Create a DataFrame
df = pd.DataFrame([track_data])

print(df)

# Optionally, save to CSV
# df.to_csv('track_features.csv', index=False)