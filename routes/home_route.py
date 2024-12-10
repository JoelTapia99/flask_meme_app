from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect

from services.file_service import save_file
from services.meme_service import search_memes, get_all
from validators.form_validator import validate_form

main = Blueprint('home_blueprint', __name__)
load_dotenv()


@main.route('/')
def hello_world():
    data = []
    query = request.args.get('query', '')
    if query:
        data = search_memes(query.strip().lower())
    else:
        data = get_all()

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
