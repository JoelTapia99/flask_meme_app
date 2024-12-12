from sqlalchemy.orm import joinedload

from exceptions.coneccion_exception import ConnectionException
from models.Meme import Meme
from sqlalchemy import or_
from utils.db import db
from utils.logger import Logger


def get_all():
    try:
        return Meme.query.options(joinedload(Meme.etiquetas)).order_by(Meme.cargada.desc()).all()
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
