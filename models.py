from myapp import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(40), unique=True)
    
    def __repr__(self):
        return '<User %r>' % self.username
    