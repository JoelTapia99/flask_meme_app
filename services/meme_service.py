from locale import str

from sqlalchemy.orm import noload, joinedload
from exceptions.coneccion_exception import ConnectionException
from models.Meme import Meme
from sqlalchemy import or_
from utils.db import db
from utils.logger import Logger


def get_all():
    try:
        return Meme.query.options(noload(Meme.etiquetas)).order_by(Meme.cargada.desc()).all()
    except Exception as e:
        Logger.error(f"Error al traer todos los memes: {str(e)}")
        raise ConnectionException("Error con la conexión a la base de datos")


def search_memes(query):
    try:
        memes = db.session.query(Meme).filter(
            or_(
                Meme.descripcion.like(f"%{query}%"),
                Meme.usuario.like(f"%{query}%")
            )
        ).all()
        return [{"descripcion": meme.descripcion, "usuario": meme.usuario, "ruta": meme.ruta} for meme in memes]
    except Exception as e:
        Logger.error(f"Error al buscar los memes: {str(e)}")
        raise ConnectionException("Error con la conexión a la base de datos")


def get_meme_by_id(meme_id):
    try:
        meme = (db.session.query(Meme)
                .options(joinedload(Meme.etiquetas))
                .filter(Meme.id == meme_id)
                .first())

        if meme:
            meme.etiquetas.sort(key=lambda etiqueta: (etiqueta.confianza is not None, etiqueta.confianza))

        return meme
    except Exception as e:
        Logger.error(f"Error al buscar un meme por id: {str(e)}")
        return None



def exist_meme(meme_id):
    try:
        meme = db.session.get(Meme, meme_id)
        return meme is not None
    except Exception as e:
        Logger.error(f"Error al verificar si existe un meme por id: {str(e)}")
