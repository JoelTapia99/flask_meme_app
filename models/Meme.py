import uuid
from datetime import datetime

from utils.db import db


class Meme(db.Model):
    __tablename__ = 'memes'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    descripcion = db.Column(db.Text, nullable=True)
    ruta = db.Column(db.Text, nullable=True)
    usuario = db.Column(db.Text, nullable=True)
    cargada = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    etiquetas = db.relationship('Etiqueta', backref='meme', cascade="all, delete-orphan", lazy=True)
