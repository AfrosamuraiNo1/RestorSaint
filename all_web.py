import csv
import re

def data_address(): # Эта функция обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    with open("data_csv/address.csv", 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';') 
    
        processed_data = {}

        for restaurant in restaurants:
            name = restaurant.get('Название организации')
            address = restaurant.get('Адрес заведения').split()
            bulding_number = address[-1]
            street_name = ' '.join(address[0:-1])
            new_pospekt = re.sub('пр.', 'проспект', street_name)
            
            if 'г.' not in address:
                processed_data[name] = f'{bulding_number} {new_pospekt} , Санкт-Петербург'
    
    return(processed_data)


def descrition_place(): # Эта функция обрабатывает описание заведения.
    with open("data_csv/address.csv", 'r') as f:
        places = csv.DictReader(f, delimiter=';')

        place_data = {}

        for place in places:
            name = place.get('Название организации')
            all_places = place.get('Описание заведения').strip()
            place_data[name] = all_places
    
    return place_data

def descrition_place(): # Эта функция обрабатывает описание заведения.
    with open("data_csv/address.csv", 'r') as f:
        places = csv.DictReader(f, delimiter=';')

        place_data = {}

        for place in places:
            name = place.get('Название организации')
            all_places = place.get('Описание заведения').strip()
            place_data[name] = all_places
    
    return place_data


def title_place(): # Эта функция обрабатывает короткое описание заведения.
    with open("data_csv/cards.csv", 'r') as f:
        title_places = csv.DictReader(f, delimiter=';')

        title_place_data = {}

        for title_place in title_places:
            name = title_place.get('Название заведения')
            title_all_places = title_place.get('Инофрмация о заведение').strip()
            title_place_data[name] = title_all_places
    
    return title_place_data
    




        
