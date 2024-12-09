from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect

from services.file_service import save_file
from services.search_service import search_memes
from validators.form_validator import validate_form

main = Blueprint('home_blueprint', __name__)
load_dotenv()


@main.route('/')
def hello_world():  # put application's code here
    data = []
    query = request.args.get('query', '')  # Obtiene el término de búsqueda
    if query:
        data = search_memes(query.strip().lower())

    # TODO: eliminar la data quemada
    # data = [
    #     {
    #         "descripcion": "Un meme divertido",
    #         "usuario": "user1",
    #         "ruta": "https://example.com/meme1.jpg"
    #     },
    #     {
    #         "descripcion": "Otro meme divertido",
    #         "usuario": "user2",
    #         "ruta": "https://example.com/meme2.jpg"
    #     }
    # ]

    return render_template('index.html', memes=data)


@main.route('/upload', methods=['POST'])
def upload():
    errors = validate_form(request)

    if errors:
        return render_template('index.html', errors=errors)

    errors = save_file(request)

    if errors:
        return render_template('index.html', errors=errors)

    return redirect('/')
