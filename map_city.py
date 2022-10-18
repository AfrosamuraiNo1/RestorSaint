from threading import local
import folium
from functools import partial
from geopy.geocoders import Nominatim
from all_web import data_address

def snt_peterburg():
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    m.save('world.html')

def geo_point():
    loc = {}
    address_point = data_address()
    for address in address_point:
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(address)
        
        location = (location.latitude, location.longitude)
        loc = dict.fromkeys(location) 
        print(loc)
          
          
     #folium.Marker(point, popup=info).add_to(m)
        

geo_point()     

'''
# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()
# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
 incidents.add_child(
 folium.features.CircleMarker(
 [lat, lng],
 radius=5, # define how big you want the circle markers to be
 color=’yellow’,
 fill=True,
 fill_color=’red’,
 fill_opacity=0.6
   )
 )
# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)
for lat, lng, label in zip(latitudes, longitudes, labels):
 folium.Marker([lat, lng], popup=label).add_to(sanfran_map) 
 
# add incidents to map
sanfran_map.add_child(incidents)'''



