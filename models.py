import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate 
#from settings import DB_NAME


db_NAME = os.environ['DB_NAME']
database_path = "postgresql:///{}".format(db_NAME)
db = SQLAlchemy()
# migrate = Migrate()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app  
    db.init_app(app)
    # migrate.init_app(app, db)
    db.create_all()


'''
Data
'''
class Movies(db.Model):
    __tablename__ = 'movielist'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date)
    movie_casting = db.relationship("Castings", secondary="collections", back_populates='castings_movie', lazy='dynamic')

   
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

class Castings(db.Model):
    __tablename__ = 'castinglist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(120))
    castings_movie = db.relationship("Movies", secondary="collections", back_populates='movie_casting', lazy='dynamic')

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
      
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,

        }


class Collections(db.Model):
    __tablename__ = 'collections'
    
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movielist.id'))
    casting_id = db.Column(db.Integer, db.ForeignKey('castinglist.id'))
