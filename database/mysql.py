import os

from dotenv import load_dotenv

from utils.logger import Logger

load_dotenv()


def create_db_uri():
    try:
        host = os.getenv('AWS_MYSQL_URL')
        user = os.getenv('AWS_MYSQL_USER')
        password = os.getenv('AWS_MYSQL_PASSWORD')
        db_name = os.getenv('AWS_MYSQL_DB_NAME')
        port = os.getenv('AWS_MYSQL_PORT')

        print(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}')
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'
    except Exception as e:
        Logger.error("Error al generar la URI de la base de datos")
        raise


def check_db_connection(app):
    try:
        if not check_db_connection(app):
            Logger.warning("No se pudo conectar a la base de datos. Verifique la configuración.")
            # raise Exception("Conexión a la base de datos fallida")

        # with app.app_context():
        #     db.session.execute('SELECT 1')
        #     Logger.info("Conexión a la base de datos establecida correctamente")
        return True
    except Exception as err:
        Logger.error("La base de datos no está activa")
        return False


# def init_db(app):
#     try:
#         app.config['SQLALCHEMY_DATABASE_URI'] = create_db_uri()
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
#
#         # db.init_app(app)
#     except Exception as e:
#         Logger.error("Error al configurar la aplicación con SQLAlchemy")
#         raise
