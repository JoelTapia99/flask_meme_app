import os

import requests
from dotenv import load_dotenv

from utils.logger import Logger

load_dotenv()


def get_tags_from_imagga(image_path):
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

            if response.status_code != 200:
                return []

            data = response.json()
            new_tags = []

            for item in data['result']['tags']:
                new_tag = {
                    'etiqueta': item['tag']['en'],
                    'confianza': item['confidence']
                }
                new_tags.append(new_tag)
            return new_tags
    except Exception as e:
        Logger.error(f"Error al procesar la imagen: {str(e)}")
