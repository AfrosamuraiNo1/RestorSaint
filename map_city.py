import folium
from functools import partial
from geopy.geocoders import Nominatim


def snt_peterburg():
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    st_peterburg = 'Санкт-Петербург'
    folium.Marker([59.939099, 30.315877], popup='Санкт-Петербург_',tooltip=st_peterburg).add_to(m)
    m.save('world.html')

def geo_point():
    geolocator = Nominatim(user_agent='Afro$amuraiNo1')
    geocode = partial(geolocator.geocode,  language='RU')
    location = geolocator.geocode('Кузьминское ш. 66, Пушкин') # г. Пушкин, Кузьминское ш. 66, Санкт-Петербург
    print((location.latitude, location.longitude))

geo_point()