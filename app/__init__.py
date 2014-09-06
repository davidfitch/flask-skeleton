from flask import Flask
from config import config
from flask.ext.sqlalchemy import SQLAlchemy

# create the database object
db = SQLAlchemy()

# this function is the application factory
def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])

    db.init_app(app)

    from bp_main import bp_main
    from bp_another_blueprint import bp_another_blueprint

    app.register_blueprint(bp_main, url_prefix='')
    app.register_blueprint(bp_another_blueprint, url_prefix='/another_bp')

    return app


