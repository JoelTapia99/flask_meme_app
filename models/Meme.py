import uuid
from datetime import datetime

from utils.db import db


class Meme(db.Model):
    __tablename__ = 'memes'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    descripcion = db.Column(db.String(255), nullable=False)
    ruta = db.Column(db.String(255), nullable=False)
    usuario = db.Column(db.String(50), nullable=False)
    cargada = db.Column(db.DateTime, default=datetime.utcnow)



