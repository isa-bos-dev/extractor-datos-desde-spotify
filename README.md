# Proyecto 1 - Extractor de datos desde Spotify

## 1. Módulo - Extracción de Información de Episodios de un podcast

Este módulo  es una herramienta que permite extraer los datos de un podcast y almacenarlos en una base de datos local. Los podcast han de estar disponibles en la plataforma de streaming Spotyfy.


### 1.1 Instalacón


### 1.1.1 Creación del ambiente virtual

Para crear el ambiente virtual utilizamos el siguiente vomando:

```bash
python -m venv nombre_ambiente_virtual
```

### 1.1.2 Activación del ambiente virtual

Para activar el ambiente virtual utilizamos el siguiente comando:


Linux/MacOS:
```bash
source nombre_ambiente_virtual/bin/activate
```


Windows:
```bash
nombre_ambiente_virtual\Scripts\activate
```


### 1.1.3 Instalación de dependencias


Para instalar las dependencias utilizamos el siguiente comando:


```bash
pip install -r requeriments.txt
```


## 1.2 Ejecución

Para utilizar esta herramienta, ejecuta el siguiente comando en tu terminal:



```bash
python main.py -c "Nombre_podcast" -i ID_Podcast -d "nombre_de_la_db.db"
```


Donde:


- `-c`: Nombre del podcast.
- `-i`: ID del podcast.
- `-d`: Nombre de la base de datos


Ejemplo:


```bash
python main.py -c "Historia en Podcast" -i 4u1nTj7G2CaNT7pZCntXvr -d "historia_podcast_episodios.db"
```


Una vez se ejecute el script se creará una base de datos con el nombre especificado en el dirctorio actual con la información de los episodios del podcast