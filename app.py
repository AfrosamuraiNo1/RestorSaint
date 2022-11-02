from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from all_web import data_address, descrition_place, title_place

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    descrition = db.Column(db.String(500))
    title = db.Column(db.String(255))


    def __repr__(self):
        return f'Place: {self.name}'


@app.route('/')
def fill_db():
    places = data_address()

    for name, address in places.items():
        query = db.select(Place).filter_by(name=name)
        exists = db.session.execute(query).first()

        if not exists:
            new_place = Place(name=name, address=address)
            db.session.add(new_place)

    db.session.commit()    

    return 'database filled'      


@app.route('/')
def descrition_db():
    places = descrition_place()

    for place_data in places.items():
        add_place = db.select(Place).filter_by(descrition=place_data)
        db.session.add(add_place)

    db.session.commit()    

    return 'database filled'


@app.route('/')
def title_db():
    places = title_place()

    for title_place_data in places.items():
        add_place = db.select(Place).filter_by(title=title_place_data)
        db.session.add(add_place)

    db.session.commit()    

    return 'database filled'    

if __name__ == '__main__':
    app.run(debug=True)              