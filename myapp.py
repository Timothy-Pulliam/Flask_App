#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager

# Initialize app. Note, this is the preferred way to load the application.
# http://flask.pocoo.org/docs/0.10/api/#flask.Request.args
app = Flask('Inventory')
app.config.from_pyfile('config.py')
# Load extensions
login_manager = LoginManager()
login_manager.init_app(app)
# In production, setting app.debug = False will disable the toolbar.
toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)