import csv

def proces_restaurants_data():
    with open('data_csv/adress.csv', 'r') as f:
        restaurants = csv.DictReader(f, delimiter=';')

        proces_data = {}

        for restaurant in restaurants:
            name = restaurant.get('Название заведения')
            address = restaurant.get('Адрес заведения').split()
            building_number = address[-1]
            street_name = ' '.join(address[0:-1])

            if 'r.' not in address:
                proces_data[name] = f'{building_number} {street_name}, Санкт-Петербург'
                
    return proces_data 