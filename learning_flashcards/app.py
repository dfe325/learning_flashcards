from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from . models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    from models import Flashcard

    @app.route('/')
    def learning_flashcards():
        return "Hello World!"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    db.init_app(app)

    app.cli.add_command(create_tables)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

