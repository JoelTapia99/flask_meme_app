from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.mysql import create_db_uri
from database.s3 import start_s3
from routes import home_route

app = Flask(__name__)

# CONFIG MYSQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = create_db_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
db = SQLAlchemy(app)

# CONFIG S3 SERVICE
app.s3_client = start_s3()

# CONFIG ROUTES
app.register_blueprint(home_route.main, url_prefix='/')
