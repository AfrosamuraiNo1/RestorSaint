import folium
from functools import partial
from geopy.geocoders import Nominatim
import csv


m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)    
m.save('world.html')

geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')

with open('adress.csv', 'r', encoding='utf-8') as adress:
    for adress in adress:
        adr = adress
        location = geolocator.geocode('adr') #не правильно передает данные из csv
        info = (location.address)
        point = ((location.latitude, location.longitude))
        folium.Marker(point, popup=info).add_to(m)
        m.save('world.html')



