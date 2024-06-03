from pytube import YouTube
from vimeo_downloader import Vimeo
import logging
import os
import json

# Configurar o logging
logging.basicConfig(filename='download.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

HISTORY_FILE = 'download_history.json'

def update_download_history(title, url, save_path):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as file:
            history = json.load(file)
    history.append({"title": title, "url": url, "path": save_path})
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        logging.info(f"Iniciando o download: {yt.title}")
        stream.download(save_path)
        logging.info(f"Download concluído: {yt.title} salvo em {save_path}")
        print(f"Download concluído! Vídeo salvo em: {save_path}")
        update_download_history(yt.title, url, save_path)
    except Exception as e:
        logging.error(f"Erro ao baixar o vídeo do YouTube: {e}")
        print(f"Erro ao baixar o vídeo do YouTube: {e}")

def download_vimeo_video(url, save_path):
    try:
        vimeo = Vimeo(url)
        stream = vimeo.streams[-1]  # Seleciona a stream de maior resolução
        logging.info(f"Iniciando o download: {vimeo.metadata.title}")
        stream.download(download_directory=save_path)
        logging.info(f"Download concluído: {vimeo.metadata.title} salvo em {save_path}")
        print(f"Download concluído! Vídeo salvo em: {save_path}")
        update_download_history(vimeo.metadata.title, url, save_path)
    except Exception as e:
        logging.error(f"Erro ao baixar o vídeo do Vimeo: {e}")
        print(f"Erro ao baixar o vídeo do Vimeo: {e}")
