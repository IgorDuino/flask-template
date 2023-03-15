import flask
from db import db_session


blueprint = flask.Blueprint(
    'pred_prof_routes',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET'])
def home_page():
    pass