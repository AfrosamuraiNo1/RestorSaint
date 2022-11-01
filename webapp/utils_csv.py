import csv
import re
from unicodedata import name
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

#print(data_address())    

def descrition_place(): # Эта функция обрабатывает описание заведения.
    with open(DATA_CSV1, 'r') as f:
        places = csv.DictReader(f, delimiter=';')

        place_data = {}

        for place in places:
            name = place.get('Название организации')
            all_places = place.get('Описание заведения').strip()
            place_data[name] = all_places
    return place_data

#print(descrition_place())


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
    name = [name for name in data_address().keys()]
    title = [name for name in title_place().values()]
    address = [name for name in data_address().values()]
    descript_place = [name for name in descrition_place().values()]
    base_restaurant(name, title, address, descript_place)



def base_restaurant(name, title, address, descript_place):
    data_restaurant = Place(name=name, title=title, address=address, descript_place=descript_place)
    db.session.add(data_restaurant)
    db.session.commit()