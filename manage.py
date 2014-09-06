#!venv/bin/python
import os
from app import create_app
from flask.ext.script import Manager, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#app.run(host='0.0.0.0')
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == '__main__':
    manager.run()
