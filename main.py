from flask import Flask

# from routes import routes
from settings import settings
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = settings.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DB_URL

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
# app.register_blueprint(routes.blueprint)


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
