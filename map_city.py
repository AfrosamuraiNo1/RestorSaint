import folium
from functools import partial
from geopy.geocoders import Nominatim
import csv


def snt_peterburg():
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    m.save('world.html')

def geo_point():
    with open('adress.csv', 'r', encoding='utf-8') as adress:
        for adress in adress:
            adr = adress
            geolocator = Nominatim(user_agent='Afro$amuraiNo1')
            geocode = partial(geolocator.geocode,  language='RU')
            location = geolocator.geocode('Кузьминское ш. 66, Пушкин') # Нужно передать adr
            point = ((location.latitude, location.longitude))
            info = (location.address)
            print(point)
            print(info)

#folium.Marker(point, popup=info).add_to(m)
