import uuid

from utils.db import db


class Etiqueta(db.Model):
    __tablename__ = 'etiquetas'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    meme_id = db.Column(db.String(36), db.ForeignKey('memes.id'), nullable=False)
    etiqueta = db.Column(db.String(50), nullable=False)
    confianza = db.Column(db.Float, nullable=False)
