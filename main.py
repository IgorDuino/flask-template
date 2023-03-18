from flask import Flask

from db import db_session

from routes import routes

app = Flask(__name__)


def init():
    db_session.global_init()
    app.register_blueprint(routes.blueprint)


init()

if __name__ == "__main__":
    app.run()
