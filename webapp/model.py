#from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

db = SQLAlchemy() 

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    title = db.Column(db.String(255))
    address = db.Column(db.String(255))
    descript_place = db.Column(db.Text)

    def __repr__(self):
        return f'Place: {self.name}{self.title}{self.address}{self.descrition_place}'