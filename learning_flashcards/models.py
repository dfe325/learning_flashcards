from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
import sqlalchemy
#from flask_sqlalchemy import SQLAlchemy

#https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#install-requirements
#https://www.twilio.com/blog/build-whatsapp-flashcard-bot-python-flask-twilio


from app import db


class Flashcard(db.Model):
    __tablename__ = 'flashcards'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    answer = db.Column(db.String())
    author = db.Column(db.String())
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, author, published):
        self.name = name
        self.author = author

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
        }