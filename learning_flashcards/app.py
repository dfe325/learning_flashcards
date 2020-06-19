from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from . models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/')
    def learning_flashcards():
        return "Hello World!"

    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'my_database',
        'host': 'localhost',
        'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()

