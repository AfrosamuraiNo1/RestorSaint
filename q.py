import folium
from functools import partial
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')
location = geolocator.geocode("Тихоокеанская ул., 10, Санкт-Петербург")
loc = (location.address)
point = (location.latitude, location.longitude)
print(loc)
print(point)