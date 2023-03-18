import flask
from db.db_session import create_session


blueprint = flask.Blueprint("preprof_routes", __name__, template_folder="templates")


@blueprint.route("/", methods=["GET"])
def home_page():
    db_sess = create_session()

    return "aboba"


@blueprint.route("/profile", methods=["GET", "POST"])
def profile_page():
    session = create_session()

    return "aboba"
