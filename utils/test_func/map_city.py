from logging import logMultiprocessing
import folium
from functools import partial
from geopy.geocoders import Nominatim
from utils.all_web import data_address


# def geo_point():
#     address_point = ['57 Литейный проспект, Caнкт-Петербург', '32 ул. Пионерская, Caнкт-Петербург', '12 ул. 1-я Советская, Caнкт-Петербург','26 Невский проспектспект, Caнкт-Петербург']# data_address()

#     point_data = {}

#     for point in address_point:
#         geolocator = Nominatim(user_agent='Afro$amuraiNo1')
#         geocode = partial(geolocator.geocode,  language='RU')
#         location = geolocator.geocode(point)
#         print(location)
    #     if location:
    #         location = (location.latitude, location.longitude)
    #         point_data[name] = location
    
    # return(point_data)

geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')
location = geolocator.geocode('57 Литейный проспект, Caнкт-Петербург')
location = (location.latitude, location.longitude)
print(location)

# def map_marker():
#     marker = geo_point()
#     name = data_name()
#     name_and_marker= dict(zip(name,marker))
#     print(name_and_marker)
    # city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    # for keys, values in name_and_marker:
    #     folium.Marker(location=values,popur=keys,icon=folium.Icon(color='green')).add_to(city)
    # return city.save('../tempalates/restaurants-spb.html')

