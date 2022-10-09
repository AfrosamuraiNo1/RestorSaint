import folium
from functools import partial
from geopy.geocoders import Nominatim

m = folium.Map(location=[59.939099, 30.315877],zoom_start=10)
st_peterburg = 'Санкт-Петербург'
folium.Marker([59.939099, 30.315877], popup='Санкт-Петербург_',tooltip=st_peterburg).add_to(m)
folium.Marker([60.0712695, 30.239394751678446], popup='10 к1, Тихоокеанская улица, Парголово, Санкт-Петербург, Северо-Западный федеральный округ, 194362, Россия',tooltip=st_peterburg).add_to(m)
m.save('world3.html')