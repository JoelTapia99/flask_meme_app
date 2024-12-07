import os

from dotenv import load_dotenv
from flask import Blueprint

main = Blueprint('home_blueprint', __name__)
load_dotenv()


@main.route('/')
def hello_world():  # put application's code here
    return f'Rutas home {os.getenv("EXAMPLE_VAR")}'
