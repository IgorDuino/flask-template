import flask
from db import db_session


blueprint = flask.Blueprint(
    'preprof_routes',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET'])
def home_page():
    return "aboba"