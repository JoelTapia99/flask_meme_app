import uuid

from utils.db import db


class Etiqueta(db.Model):
    __tablename__ = 'etiquetas'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    meme_id = db.Column(db.String(36), db.ForeignKey('memes.id', ondelete='CASCADE', onupdate='CASCADE'))
    etiqueta = db.Column(db.Text, nullable=True)
    confianza = db.Column(db.Float, nullable=True)
