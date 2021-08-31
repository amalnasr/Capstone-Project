import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

# database_name = "capstoneproject"
# database_path = "postgresql://{}@{}/{}".format('postgres:1996', 'localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app,db)
    

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # add one demo row which is helping in POSTMAN test
    actor = Actor(
        name='actor name',
        age='25',
        gender='actor gender',
    )
    actor.create()

    movie = Movie(
        title='movie title',
        release_date='2012-12-12'
        
    )
    movie.create() 


class Movie(db.Model):
    __tablename__ = 'Movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(db.DateTime, nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def create(self):
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
            'release date': self.release_date
        }
class Actor(db.Model):
    __tablename__ = 'Actors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age,  gender):
        self.name = name
        self.age = age
        self.gender = gender

    def create(self):
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
            'gender': self.gender
        }