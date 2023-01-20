import csv
import re

from webapp.config import DATA_CSV1, DATA_CSV2
from functools import partial
from geopy.geocoders import Nominatim


def data_base():
    merged_data = {}

    with open(DATA_CSV1, 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';')
        for restaurant in restaurants:
            name = restaurant.get('Название организации')
            description = restaurant.get('Описание заведения').strip()
            description = re.sub('\xa0', ' ', description)
            description = re.sub('\n', ' ', description)
            address = restaurant.get('Адрес заведения').split() # ['пр.', 'Маршала', 'Блюхера', '6']
            geolocator = Nominatim(user_agent='Afro$amuraiNo1')
            geocode = partial(geolocator.geocode,  language='RU')
            location = geolocator.geocode(address)
            if not location:
                bulding_number = address[-1]  # 54-56
                street_name = ' '.join(address[0:-1])  # пр. Маршала Блюхера
                new_pospekt = re.sub('пр/.', 'проспект', street_name)
                full_address = f'{bulding_number} {new_pospekt} , Санкт-Петербург'
                merged_data[name] = {
                    'address': full_address,
                    'description': description,
                }
            else:
                address = restaurant.get('Адрес заведения')
                full_address = f'{address} , Санкт-Петербург'
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