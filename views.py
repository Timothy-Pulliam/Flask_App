from myapp import app, db
from models import User
from sqlalchemy import exc
from flask import render_template, redirect, flash
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/', methods=['POST', 'GET'])
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegistrationForm()
    try:
        if form.validate_on_submit():
            # Redirect to Dash Board if all form information is validated according
            # to form validation rules
            new_user = User(username=form.username.data, 
                            password=generate_password_hash(form.password.data,method='sha256'),
                            email=form.email.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/dashboard')
    except exc.IntegrityError as e:
        flash("Username or Email already taken. Try another one.", 'error')
    return render_template("signup.html", form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    # TODO Figure out right combination of if statements to make flash statement work
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if bool(user) and (user.username == form.username.data) and check_password_hash(user.password, form.password.data):
            return redirect('/dashboard')
        else:
            flash('invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route('/<string:username>')
def home(username):
    return render_template('home.html', username=username)