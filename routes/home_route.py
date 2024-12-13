from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect

from exceptions.coneccion_exception import ConnectionException
from services.file_service import save_file
from services.meme_service import search_memes, get_all, exist_meme, get_meme_by_id
from validators.form_validator import validate_form

main = Blueprint('home_blueprint', __name__)
load_dotenv()


@main.route('/')
def hello_world():
    data = []
    try:
        query = request.args.get('query', '')
        if query:
            data = search_memes(query.strip().lower())
        else:
            data = get_all()

        return render_template('index.html', memes=data)
    except ConnectionException as ce:
        server_error = str(ce)
        return render_template('index.html', memes=data, serverError=server_error)


@main.route('/upload', methods=['POST'])
def upload():
    errors = validate_form(request)

    if errors:
        return render_template('index.html', errors=errors)

    errors = save_file(request)

    if errors:
        return render_template('index.html', errors=errors)

    return redirect('/')

@main.route('/<string:id>', methods=['GET'])
def find_by_id(id):
    exist = exist_meme(id)
    if exist is None:
        return render_template('details.html', memes=[])

    meme = get_meme_by_id(id)

    return render_template('details.html', meme=meme)
