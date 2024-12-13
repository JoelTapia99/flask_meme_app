from app import app
from database.mysql import check_db_connection

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    check_db_connection(app)
