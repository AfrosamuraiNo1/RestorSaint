import csv
import re


def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
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
    
    return processed_data

