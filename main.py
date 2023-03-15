from flask import Flask
from db import db_session
from routes import routes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


def init():
    db_session.global_init()    # Подключение к БД
    app.register_blueprint(routes.blueprint)



init()


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')