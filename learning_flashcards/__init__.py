'''from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()

import learning_flashcards.views
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/flashcards''''

from flask import Flask

from .commands import create_tables
from .extensions import db
from .models import User

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.login_view = 'auth.login'

    app.cli.add_command(create_tables)

    return app