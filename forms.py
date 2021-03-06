from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired, ValidationError

class RegistrationForm(FlaskForm):
    username = TextField('username', validators=[InputRequired(), Length(min=4, max=30)])
    email = TextField('email', validators=[InputRequired(), Email(), Length(max=40)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [DataRequired()])


class LoginForm(FlaskForm):
    username = TextField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')
