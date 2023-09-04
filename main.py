import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Autenticación
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Haz una solicitud a la API, por ejemplo, buscar un álbum
results = sp.search(q='A Night at the Opera artist:Queen', type='album')
albums = results['albums']['items']  # Cambié 'itmes' a 'items'

for album in albums:
    print(album['name'], album['release_date'])
                                          