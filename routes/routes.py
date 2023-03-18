import flask
from flask import render_template
from db.db_session import create_session


blueprint = flask.Blueprint("preprof_routes", __name__, template_folder="templates")


@blueprint.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")


@blueprint.route("/profile", methods=["GET", "POST"])
def profile_page():
    session = create_session()

    return "aboba"
