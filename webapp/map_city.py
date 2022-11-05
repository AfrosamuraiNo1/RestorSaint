import folium
from functools import partial
from geopy.geocoders import Nominatim
from webapp.utils_csv import data_address


def geo_point(): #Создаёт из адресов гео точки с именами заведений.
    address_point = data_address()
    point_data = {}

    for name, point in address_point.items():
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(point)
        if location:
            location = (location.latitude, location.longitude)
            point_data[name] = location    
    return point_data


def map_marker(): #Cоздаёт на карте точки с именами.
    name_and_marker = geo_point()
    city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    for keys, values in name_and_marker.items():
        folium.Marker(location=values,popup=keys,icon=folium.Icon(color='green')).add_to(city)
    return city.save('tempalates/restaurants-spb.html')