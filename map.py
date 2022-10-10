import folium
from functools import partial
from geopy.geocoders import Nominatim

def snt_peterburg():
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    folium.Marker(point, popup=loc).add_to(m)
    folium.Marker(point1, popup=loc1).add_to(m)
    folium.Marker(point2, popup=loc2).add_to(m)
    m.save('map.html')
    
geolocator = Nominatim(user_agent='Afro$amuraiNo1')
geocode = partial(geolocator.geocode,  language='RU')
location = geolocator.geocode("Адмирала Черокова ул., 18, Санкт-Петербург")
location1 = geolocator.geocode("Тихоокеанская ул., 10, Санкт-Петербург")
location2 = geolocator.geocode("Кузьминское ш., 66, Пушкин")
loc = (location.address)
loc1 = (location1.address)
loc2 = (location2.address)
point = ((location.latitude, location.longitude))
point1 = ((location1.latitude, location1.longitude))
point2 = ((location2.latitude, location2.longitude))
   

snt_peterburg() 