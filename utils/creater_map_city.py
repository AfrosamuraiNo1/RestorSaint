import folium
from functools import partial
from geopy.geocoders import Nominatim
from csv_agrigator import data_base
import re

from folium.plugins import MarkerCluster
from folium.plugins import Search


def map_marker(): #Cоздаёт на карте точки с именами.
    name_and_marker = geo_point()
    city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    for keys, values in name_and_marker.items():
        folium.Marker(location=values,popup=keys,icon=folium.Icon(color='green')).add_to(city)
    return city.save('tempalates/restaurants-spb.html')


def geo_point(): #Создаёт из адресов гео точки с именами заведений.
    old_data = data_base()
    merged_data = {}
    for name, data in old_data.items():
        description = data['description']
        info = data['info']
        address = data['address']
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(address)
        if location:
            location = location.latitude,location.longitude
            merged_data[name] = {
            'address': address,
            'description': description,
            'info': info,
            'latitude': location[0],
            'longitude': location[1]
            }
    return merged_data

a = geo_point()
for names, value in a.items():
    print(names[1])

def map_marker(): #Cоздаёт на карте точки с именами.
    name_and_marker = geo_point()
    city = folium.Map(location=[59.939099, 30.315877],zoom_start=11)
    for keys, values in name_and_marker.items():
        folium.Marker(location=values,popup=keys,icon=folium.Icon(color='green')).add_to(city)
    return city.save('tempalates/restaurants-spb.html')


def visualize_locations_with_marker_cluster():
    name_and_marker = geo_point()
    f = folium.Figure(width=1000, height=500)
    m = folium.Map(location=[59.939099, 30.315877],zoom_start=11).add_to(f)
    marker_cluster = MarkerCluster().add_to(m)

    for keys, values in name_and_marker.items():
        folium.Marker(location=values,popup=keys,name=keys,icon=folium.Icon(color='green')).add_to(marker_cluster)

    servicesearch = Search(
        layer=marker_cluster,
        search_label="name",
        placeholder='Search for a service',
        collapsed=False,
        search_zoom=20,
    ).add_to(m)


    return m.save('spb.html')