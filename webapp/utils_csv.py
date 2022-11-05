import csv
from distutils.log import info
import re
from webapp.model import db, Place
from webapp.config import DATA_CSV1, DATA_CSV2


def data_address(): # Эта функция обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    with open(DATA_CSV1, 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';') 
    
        processed_data = {}

        for restaurant in restaurants:
            name = restaurant.get('Название организации')
            address = restaurant.get('Адрес заведения').split()
            bulding_number = address[-1]
            street_name = ' '.join(address[0:-1])
            new_pospekt = re.sub('пр.', 'проспект', street_name)
            full_address = f'{bulding_number} {new_pospekt} , Санкт-Петербург'
            
            if 'г.' not in address:
                processed_data[name] = full_address
    return processed_data


def descrition_place(): # Эта функция обрабатывает описание заведения.
    with open(DATA_CSV1, 'r') as f:
        places = csv.DictReader(f, delimiter=';')

        place_data = {}

        for place in places:
            name = place.get('Название организации')
            all_places = place.get('Описание заведения').strip()
            all_places = re.sub('\xa0',' ', all_places)
            all_places = re.sub('\n',' ', all_places)
            place_data[name] = all_places
    return place_data


def title_place(): # Эта функция обрабатывает короткое описание заведения.
    with open(DATA_CSV2, 'r') as f:
        title_places = csv.DictReader(f, delimiter=';')

        title_place_data = {}

        for title_place in title_places:
            name = title_place.get('Название заведения')
            title_places = title_place.get('Инофрмация о заведение').strip()
            title_place_data[name] = title_places
    return title_place_data


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
            new_prospekt = re.sub('пр.', 'проспект', street_name)
            full_address = f'{bulding_number} {new_prospekt} , Санкт-Петербург'
            
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

def base_restaurant():
    places = data_base()

    for name, data in places.items():
        address = data['address']
        description = data['description']
        info = data['info']

        query = db.select(Place).filter_by(name=name)
        exists = db.session.execute(query).first()

        if not exists:
            new_place = Place(
                name=name,
                address=address,
                description=description,
                info=info,
            )
            db.session.add(new_place)
    db.session.commit()
    return 'well done'

