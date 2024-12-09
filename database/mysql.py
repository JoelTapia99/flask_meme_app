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
        Logger.error(f"Error al generar la URI de la base de datos: {str(e)}")
        raise


def check_db_connection(app):
    try:
        if not check_db_connection(app):
            Logger.warning("No se pudo conectar a la base de datos. Verifique la configuración.")
        return True
    except Exception as err:
        Logger.error(f"La base de datos no está activa: {str(err)}")
        return False
