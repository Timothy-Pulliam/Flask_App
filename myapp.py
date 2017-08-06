#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail

# Initialize app. Note the preferred way to instantiate a Flask()
# object is by passing it the name of the package this module resides in.
# http://flask.pocoo.org/docs/0.10/api/#flask.Request.args
app = Flask('Inventory')
app.config.from_pyfile('config.py')
# Load extensions
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)
# In production, setting app.debug = False will disable the toolbar.
# This can be done in the config.py file.
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)