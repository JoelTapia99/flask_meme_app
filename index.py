from app import app
from database.mysql import check_db_connection

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    check_db_connection(app)
