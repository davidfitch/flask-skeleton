from datetime import datetime
from . import db


"""
class MyTestClass(db.Model):
    __tablename__ = 'mytesttable'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(128))
    location = db.Column(db.String(64))
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    bio = db.Column(db.Text())

    def __init__(self, email, username):
        self.email = email
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username
"""



