from flask import Blueprint

bp_another_blueprint = Blueprint('bp_another_blueprint', __name__, template_folder='templates')

from . import views, errors

