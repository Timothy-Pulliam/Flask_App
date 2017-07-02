#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_pyfile('config.py')
toolbar = DebugToolbarExtension(app)

# Establish Database Connection
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
