from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .commands import create_tables
from .extensions import db

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    db = SQLAlchemy(app)

    from models import Flashcard

    @app.route('/')
    def learning_flashcards():
        return "Hello World!"

    app.cli.add_command(create_tables)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

