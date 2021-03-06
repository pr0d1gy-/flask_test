from flask_login import UserMixin

from database_manager import DatabaseManager


db = DatabaseManager.db


class User(db.Model, UserMixin):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True
    )

    password = db.Column(
        db.String(50)
    )

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User id={} username={}>'.format(self.id, self.username)
