#!/usr/bin/env python
import settings
from database_manager import DatabaseManager
from application_manager import ApplicationManager

from flask import Flask
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


app = Flask(
    'Weather test',
    template_folder=settings.TEMPLATES_FOLDER,
    static_folder=settings.STATIC_FOLDER,
)


app.debug = settings.DEBUG
app.secret_key = settings.SECRET_KEY
app.config.from_object(settings.ConfigApp)

db = DatabaseManager.setup_db(app=app)
migrate = Migrate(app, db)

# Load blueprints
ApplicationManager.register_applications(app=app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    host=settings.HOST, port=settings.PORT))


if __name__ == '__main__':
    manager.run()
