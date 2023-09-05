import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Autenticación
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Obtener token
TOKEN = client_credentials_manager.get_access_token(as_dict=False)

#ID del podcast
podcast_id = '768GVwxeh1o6kD5bD0qJeJ'

#Obtener token
token_info = client_credentials_manager.get_access_token(as_dict=False)
access_token = token_info


# PERFORM THE QUERY

id = podcast_id      #<------------------------------------ INSERT SHOW ID MANUALLY
type = 'episodes'
market  = 'US'
limit = 50
offset = 0

id_list = []
dur_list = []
date_list = []
name_list = []
desc_list = []

counter = 0
more_runs = 1

search = 'Filosofía de bolsillo'

while(counter <= more_runs):


    endpoint_url = f"https://api.spotify.com/v1/shows/{id}/episodes?"


    query = f'{endpoint_url}'
    query += f'&q={search}'
    query += f'&type={type}'
    query += f'&offset={offset}'
    query += f'&market={market}'
    query += f'&limit={limit}'


    response = requests.get(query, 
                   headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {access_token}"})
    json_response = response.json()



    for i in range(len(json_response['items'])):

        id_list.append(json_response['items'][i]['id'])
        dur_list.append(json_response['items'][i]['duration_ms'])
        date_list.append(json_response['items'][i]['release_date'])    
        name_list.append(json_response['items'][i]['name'])
        desc_list.append(json_response['items'][i]['description'])
        
        
    more_runs = (json_response['total'] // 50 )         
        
    counter += 1
    
    offset = offset + 50   

    for n in name_list:
        print(n)
        print()                