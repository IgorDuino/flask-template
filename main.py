from flask import Flask

from db import db_session

# from routes import routes

app = Flask(__name__)


def init():
    db_session.global_init()    # Подключение к БД
    app.register_blueprint(routes.blueprint)


if __name__ == "__main__":
    main()
