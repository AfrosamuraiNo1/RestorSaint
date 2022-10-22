from threading import local
from unittest import result
import folium
from functools import partial
from geopy.geocoders import Nominatim
from all_web import data_address

def geo_point():
    loc = []
    address_point = data_address()
    for address in address_point:
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(address)
        if location:
            location = (location.latitude, location.longitude)
            loc.append(location)
    return loc   


def map_marker():
    marker = geo_point()
    city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    for markers in marker:
        folium.Marker(location=markers, icon=folium.Icon(color='green')).add_to(city)
    return city.save('restaurants-spb.html')

        

if __name__ == "__main__":
    map_marker()
