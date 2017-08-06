from myapp import db
from flask_login import UserMixin


# Any changes to models will need to followed with a subsiquent
# DB migratation https://flask-migrate.readthedocs.io/en/latest/

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    firstname = db.Column(db.String(40), nullable=True)
    lastname = db.Column(db.String(40), nullable=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    role = db.Column(db.String(1), nullable=True)
    
    def __init__(self, username, password, email, role='S'):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
    
    def __repr__(self):
        return '<User %r>' % self.username
        
    def as_dict(self):
        '''Returns User object's attributes in a list dictionary format so they can be converted into
        JSON. User's password is not included for obvious secerity reasons.'''
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'password'}
        
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(40), unique=True, nullable=False)
    start_date = db.Column(db.DateTime(), nullable=False)
    end_date = db.Column(db.DateTime(), nullable=False)
    
    def __repr__(self):
        return '<Course %r>' % self.course_name
        
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    