from logging import logMultiprocessing
import folium
from functools import partial
from geopy.geocoders import Nominatim
#from all_web import data_address


def geo_point():
    address_point = data_address()
    for key, value in list(address_point.items()):
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(value)
        if location:
            location = (location.latitude, location.longitude)
            address_point[key] = location
    return address_point

geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')
location = geolocator.geocode('12, 1-я Советская, Санкт-Петербург') #'ул. Наличная 24к1, Санкт-Петербург' 'ул. Гороховая 49б, Санкт-Петербург' 'пр. Приморский 72, Санкт-Петербург'
location = (location.latitude, location.longitude) #Наличная ул., 24, Санкт-Петербург, ул. Гороховая ул., 49 Санкт-Петербург, 'Приморский пр.72, Санкт-Петербург','Загородный проспект,15, Санкт-Петербург'
print(location)


def map_marker():
    marker = geo_point()
    name = data_name()
    name_and_marker= dict(zip(name,marker))
    print(name_and_marker)
    # city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    # for keys, values in name_and_marker:
    #     folium.Marker(location=values,popur=keys,icon=folium.Icon(color='green')).add_to(city)
    # return city.save('../tempalates/restaurants-spb.html')

        

#if __name__ == "__main__":
#    map_marker()
