import myapp
from myapp import app
import flask
import forms
import models
from sqlalchemy import exc
import werkzeug
import flask_login


@myapp.app.route('/', methods=['POST', 'GET'])
@myapp.app.route('/signup', methods=['POST', 'GET'])
def signup():
    
    form = forms.RegistrationForm()
    try:
        if form.validate_on_submit():
            new_user = models.User(
                                   username=form.username.data,
                                   password=werkzeug.security.generate_password_hash(
                                                                                    form.password.data,
                                                                                    method='sha256'
                                                                                    ),
                                   email=form.email.data
                                   )
            myapp.db.session.add(new_user)
            myapp.db.session.commit()
            #msg = myapp.mail.Message("Thank you for signing up!",
            #                 recipients=[new_user.email])
            #myapp.mail.send(msg)
            return flask.redirect('/login')

    except exc.IntegrityError as e:
        flask.flash("Username or Email already taken. Try another one.", 'error')
    return flask.render_template("signup.html", form=form)



@myapp.app.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        
        user = models.User.query.filter_by(username=form.username.data).first()
        if (user is not None) and (form.username.data == user.username) and (werkzeug.security.check_password_hash(user.password, form.password.data)):
            # Remember me option prevents user from accidently logging themselves out if they
            # close their browser (I.E. they won't have to log back in).
            flask_login.login_user(user, remember=form.remember.data)
            flask.flash('Logged in successfully.')

            next = flask.request.args.get('next')
            # is_safe_url should check if the url is safe for flask.redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            if not is_safe_url(next):
                return flask.abort(400)
                # Where should user be redirected after login?
            return flask.redirect(next or flask.url_for('dashboard'))
        else:
            flask.flash('username or password incorrect')
            return flask.render_template('login.html', form=form)

    return flask.render_template('login.html', form=form)


@myapp.app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.redirect('/login')


@myapp.app.route('/dashboard')
@flask_login.login_required
def dashboard():
    return flask.render_template('dashboard.html')

@myapp.app.route('/me', methods=['GET'])
@flask_login.login_required
def userInfo():
    return flask.jsonify(flask_login.current_user.as_dict())

@myapp.app.errorhandler(404)
def page_not_found(error):
    return flask.render_template("404.html"), 404


@myapp.login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter(models.User.id == int(user_id)).first()


def is_safe_url(next):
    #TODO implement is_url_safe http://flask.pocoo.org/snippets/62/
    return True
