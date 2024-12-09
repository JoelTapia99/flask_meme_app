from models.Meme import Meme


def search_memes(query):
    print(query)
    # Buscar coincidencias parciales en la base de datos
    memes = Meme.query.filter(Meme.descripcion.ilike(f"%{query}%")).all()
    print(memes)
    # Formatear los resultados
    return [{"descripcion": meme.descripcion, "usuario": meme.usuario, "ruta": meme.ruta} for meme in memes]
