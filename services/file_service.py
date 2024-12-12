import os

from dotenv import load_dotenv

from constants.file import UPLOAD_FOLDER
from database.s3 import s3_config
from models.Etiqueta import Etiqueta
from models.Meme import Meme
from services.imagga_service import get_tags_from_imagga
from utils.db import db
from utils.logger import Logger

load_dotenv()


def save_file(request):
    try:
        file = request.files.get('file')
        description = request.form.get('description')
        user = request.form.get('name')
        tags = get_tags(request.form.getlist('tags'))

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        s3_url = upload_file_to_s3(file, file_path)
        tags_res = get_tags_from_imagga(file_path)

        if 'error' in tags_res:
            os.remove(file_path)
            return ['Error al analizar la imagen']

        meme = Meme(descripcion=description, ruta=s3_url, usuario=user)
        db.session.add(meme)
        db.session.commit()

        tags_to_save = []
        for tag in tags_res:
            new_tag = Etiqueta(meme_id=meme.id, etiqueta=tag['etiqueta'], confianza=tag['confianza'])
            tags_to_save.append(new_tag)

        for tag in tags:
            new_tag = Etiqueta(meme_id=meme.id, etiqueta=tag, confianza=None)
            tags_to_save.append(new_tag)

        db.session.bulk_save_objects(tags_to_save)

        db.session.commit()
        os.remove(file_path)

    except Exception as e:
        db.session.rollback()
        Logger.error(f"Error al subir y analizar la imagen: {str(e)}")


def upload_file_to_s3(file, file_path):
    try:
        buket_name = os.getenv('AWS_S3_BUCKET_NAME')
        buket_region = os.getenv('AWS_S3_REGION')

        s3_client = s3_config()
        s3_client.upload_fileobj(
            open(file_path, 'rb'),
            buket_name,
            file.filename,
            ExtraArgs={"ContentType": file.content_type}
        )

        return f"https://{buket_name}.s3.{buket_region}.amazonaws.com/{file.filename}"
    except Exception as e:
        Logger.error(f"Error al subir el archivo a S3: {str(e)}")


def get_tags(tags):
    tags_list = []

    for tag in tags:
        sub_str = tag.split(',')
        for value in sub_str:
            tags_list.append(value.strip())

    return tags_list
