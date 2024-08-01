import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_track(query, limit=10):
    """
    Search for tracks on Spotify and return their IDs and information.
    
    :param query: Search query (e.g., "song name artist")
    :param limit: Maximum number of results to return (default 10)
    :return: List of dictionaries containing track information
    """
    results = sp.search(q=query, type='track', limit=limit) 
    
    tracks = []
    for track in results['tracks']['items']:
        track_info = {
            'id': track['id'],
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity']
        }
        tracks.append(track_info)
    
    return tracks

# Example usage
search_query = "Khong Con Ice"
results = search_track(search_query, limit=5)

# print(f"Search results for '{search_query}':")
# for i, track in enumerate(results, 1):
#     print(f"{i}. '{track['name']}' by {track['artist']}")
#     print(f"   Track ID: {track['id']}")
#     print(f"   Album: {track['album']}")
#     print(f"   Release Date: {track['release_date']}")
#     print(f"   Popularity: {track['popularity']}")
#     print()

# Get the track ID of the first result
if results:
    first_track_id = results[0]['id']
    print(f"Track ID of the first result: {first_track_id}")
else:
    print("No results found.")