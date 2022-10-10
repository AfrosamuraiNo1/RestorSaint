import folium
from functools import partial
from geopy.geocoders import Nominatim


m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)    
m.save('world.html')


geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')
location = geolocator.geocode("Тихоокеанская ул., 10, Санкт-Петербург")
loc = (location.address)
point = ((location.latitude, location.longitude))

for loc, point in loc, point:
    folium.Marker(loc, popup=point).add_to(m)
