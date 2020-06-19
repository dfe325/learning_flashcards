from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

import learning_flashcards.views
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/flashcards'

