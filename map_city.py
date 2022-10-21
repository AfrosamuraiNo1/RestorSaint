import folium
from functools import partial
from geopy.geocoders import Nominatim
from all_web import data_address


def snt_peterburg(): #Общая карта Санкт-Петербурга
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    st_peterburg = 'Санкт-Петербург'
    folium.Marker([59.939099, 30.315877], popup='Санкт-Петербург_',tooltip=st_peterburg).add_to(m)
    m.save('world.html')

def geo_point(): #Получает из карты координаты
    loc = []
    for address in data_address():
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')        
        location = geolocator.geocode(address) 
        if location:
            location = (location.latitude, location.longitude)
            loc.append(location)
    return loc