from flask import render_template
from . import bp_another_blueprint

@bp_another_blueprint.route('/')
def index():
    return render_template('bp_another_blueprint/index.html')

@bp_another_blueprint.route('/link1')
def link1():
    return render_template('bp_another_blueprint/link1.html')

@bp_another_blueprint.route('/link2')
def link2():
    return render_template('bp_another_blueprint/link2.html')
