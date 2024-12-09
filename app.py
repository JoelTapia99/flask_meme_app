from flask import Flask

from database.mysql import create_db_uri
from routes import home_route
from utils.db import db

app = Flask(__name__)

# CONFIG MYSQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = create_db_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
db.init_app(app)

# CONFIG ROUTES
app.register_blueprint(home_route.main, url_prefix='/')
