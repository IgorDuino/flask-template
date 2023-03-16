from flask import Flask

from db import db_session

# from routes import routes

app = Flask(__name__)


def main():
    db_session.global_init()
    app.run(port=8080, host="0.0.0.0")


if __name__ == "__main__":
    main()
