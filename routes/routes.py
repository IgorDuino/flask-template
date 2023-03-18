import flask
from flask import render_template


blueprint = flask.Blueprint("preprof_routes", __name__, template_folder="templates")


@blueprint.route("/", methods=["GET"])
def home_page():
    return render_template('index.html')

