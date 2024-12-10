import os

import requests
from dotenv import load_dotenv

from utils.logger import Logger

load_dotenv()


def get_tags_from_imagga(image_path):
    # Abre el archivo como un stream y no lo cierra automáticamente
    try:
        api_key = os.getenv('IMAGGA_API_KEY')
        api_secret = os.getenv('IMAGGA_API_SECRET')
        endpoint = os.getenv('IMAGGA_ENDPOINT')

        with open(image_path, 'rb') as image_file:
            response = requests.post(
                endpoint,
                auth=(api_key, api_secret),
                files={'image': image_file}
            )
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    except Exception as e:
        Logger.error(f"Error al procesar la imagen: {str(e)}")
