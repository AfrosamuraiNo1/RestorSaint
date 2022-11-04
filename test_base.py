import os
import csv
import re
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

DATA_CSV1 = os.path.join(basedir, 'data_csv', 'address.csv')
DATA_CSV2 = os.path.join(basedir, 'data_csv', 'cards.csv')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    info = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f'Place: {self.name}'

def data_base():
    merged_data = {}

    with open(DATA_CSV1, 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';')

        for restaurant in restaurants:
            name = restaurant.get('Название организации')
            description = restaurant.get('Описание заведения').strip()
            description = re.sub('\xa0',' ', description)
            description = re.sub('\n',' ', description)
            address = restaurant.get('Адрес заведения').split()
            bulding_number = address[-1]
            street_name = ' '.join(address[0:-1])
            new_pospekt = re.sub('пр.', 'проспект', street_name)
            full_address = f'{bulding_number} {new_pospekt} , Санкт-Петербург'
            
            if 'г.' not in address:
                merged_data[name] = {
                    'address': full_address,
                    'description': description,
                }

    with open(DATA_CSV2, 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';')

        for restaurant in restaurants:
            name = restaurant.get('Название заведения')
            info = restaurant.get('Инофрмация о заведение')
            if merged_data.get(name):
                merged_data[name]['info'] = info
    
    return merged_data
    

@app.route('/')
def index():
        
    places = data_base()

    for name, data in places.items():
        address = data['address']
        description = data['description']
        info = data['info']

        query = db.select(Place).filter_by(name=name)
        exists = db.session.execute(query).first

        if not exists:
            new_place = Place(
                name=name,
                address=address,
                description=description,
                info=info,
            )
            db.session.add(new_place)
    
    db.session.commit()

    return 'database filled'

if __name__ == '__main':
    app.run(debug=True)