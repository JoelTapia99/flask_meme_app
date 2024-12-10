from models.Meme import Meme


def search_memes(query):
    memes = Meme.query.filter(Meme.descripcion.ilike(f"%{query}%")).all()
    return [{"descripcion": meme.descripcion, "usuario": meme.usuario, "ruta": meme.ruta} for meme in memes]
