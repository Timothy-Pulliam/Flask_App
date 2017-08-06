from myapp import app
from models import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#app = Flask('Inventory')
#app.config.from_pyfile('config.py')

# Note, we are using db from the models.py file. This is the
# db object where all models objects are stored.
migrate = Migrate(app, db)
# manager allows us to run database migrations command line arguments using our flask app (myapp.py)
# python manage.py db migrate
# python manage.py db upgrade
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()