from models.Meme import Meme
from sqlalchemy import or_
from utils.db import db
from utils.logger import Logger


def get_all():
    try:
        return db.session.query(Meme).all()
    except Exception as e:
        Logger.error(f"Error al traer todos los memes: {str(e)}")


def search_memes(query):
    memes = db.session.query(Meme).filter(
        or_(
            Meme.descripcion.like(f"%{query}%"),
            Meme.usuario.like(f"%{query}%")
        )
    ).all()
    return [{"descripcion": meme.descripcion, "usuario": meme.usuario, "ruta": meme.ruta} for meme in memes]
