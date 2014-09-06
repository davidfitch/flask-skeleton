from flask import render_template
from . import bp_main

@bp_main.route('/')
def index():
    return render_template('bp_main/index.html')

@bp_main.route('/link1')
def link1():
    return render_template('bp_main/link1.html')

@bp_main.route('/link2')
def link2():
    return render_template('bp_main/link2.html')