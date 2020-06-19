from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#install-requirements
#https://www.twilio.com/blog/build-whatsapp-flashcard-bot-python-flask-twilio
''' 
class BaseModel(db.Model):
"""Base data model for all objects"""
__abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models

class YourModel(BaseModel):
"""model for one of your table"""
    __tablename__ = 'my_table'
    # define your model

'''