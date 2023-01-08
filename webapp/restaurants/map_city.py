import folium
from functools import partial
from geopy.geocoders import Nominatim
from webapp.utils_csv import data_address


from folium.plugins import MarkerCluster
from folium.plugins import Search

def geo_point(): #Создаёт из адресов гео точки с именами заведений.
    address_point = data_address()
    point_data = {}

    for name, point in address_point.items():
        geolocator = Nominatim(user_agent='Afro$amuraiNo1')
        geocode = partial(geolocator.geocode,  language='RU')
        location = geolocator.geocode(point)
        if location:
            location = (location.latitude, location.longitude)
            point_data[name] = location    
    return(point_data)



def visualize_locations_with_marker_cluster(): #Cоздаёт на карте точки с именами.
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


    return m.save('static/restaurants-spb.html')