import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

class Episodio:
    """
    Representa un episodio de un podcast.
    """
    def __init__(self, item_id, duration_ms, release_date, name, description):
        """
        Inicializa un episodio.

        Args:
            item_id (str): ID del episodio
            duduration_ms (int): Duración del episodio en milisegundos
            relrelease_date (str): Fecha de lanzamiento del episodio.
            name (str): Nombre del episodio.
            dedescription (str): Descripción del episodio.

        """
        self.item_id = item_id
        self.duration_ms = duration_ms
        self.release_date = release_date
        self.name = name
        self.description = description

    def __str__(self):
        """
        Devuelve una representación en string del episodio.

        Returns:
            str: Representación en string del episodio.
        """
        return f"Episodio(Id: {self.item_id}\nDuration (ms): {self.duration_ms}\nRelease Date: {self.release_date}\nName: {self.name}\nDescription: {self.description})"
    
    def __repr__(self):
        """
        Devuelve una representación en string del episodio.

        Returns:
            str: Representación en string del episodio.
        """
        return self.__str__()


def obtener_claves_secretas():
    """
    Obtiene las claves secretas de Spotify desde un archivo .env

    Returns:
        client_id (str): ID de la aplicación Spotify.
        client_secret (str): Clave secreta de la aplicación Spotify
    """
    load_dotenv()
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
    return client_id, client_secret

def iniciar_sesion_spotify(client_id, client_secret):
    """
    Inicia sesioón en Spotify

    Args: 
        client_id (str): ID de la aplicación Spotify.
        client_secret (str): Clave secreta de la aplicación Spotify
    Returns:
        sp (spotipy.Spotify.Spotify). Objeto de sesión de Spotify
    """
     
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    return sp, client_credentials_manager.get_access_token(as_dict=False)

def extraer_episodios_podcast(podcast_id, search, access_token):
    """
    Extrae los episodios de un podcast.

    Args: 
        client_id (str): ID de la aplicación Spotify.
        search (str): Término de búsqueda
        access_token: Token de acceso de Spotify
    Returns:
        dict: Diccionario con los datos de los episodios
    """
    id = podcast_id
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

    episodios = []

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

            episodio = Episodio(
                item_id=json_response['items'][i]['id'],
                duration_ms=json_response['items'][i]['duration_ms'],
                release_date=json_response['items'][i]['release_date'],
                name=json_response['items'][i]['name'],
                description=json_response['items'][i]['description']
            )
            episodios.append(episodio)
            
            
        more_runs = (json_response['total'] // 50 )         
            
        counter += 1
        
        offset = offset + 50   
    
    return episodios

def main():

    client_id, client_secret = obtener_claves_secretas()
    sp, access_token = iniciar_sesion_spotify(client_id, client_secret)

    search = 'Filosofía de bolsillo'
    podcast_id = '768GVwxeh1o6kD5bD0qJeJ' 

    episodios = extraer_episodios_podcast(podcast_id, search, access_token) 

    print(len(episodios))

if __name__ == '__main__':
    main() 