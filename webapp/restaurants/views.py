from flask import Blueprint, render_template, flash
from webapp.db import db
import folium
import os
from .models import Place

blueprint = Blueprint('restaurants', __name__)

@blueprint.route("/")
def index():
    title = "Рестораны Санкт-Петербурга"
    name = Place.query.all()
    return render_template('restaurant/index.html', title=title, name_list=name)

@blueprint.route("/<name>")
def about(name):
    restaurant = db.one_or_404(db.select(Place).filter_by(name=name))
    latitude = restaurant.latitude  # Передаем из базы широту
    longitude = restaurant.longitude  # Передаем из базы долготу
    city = folium.Map(location=[latitude, longitude],
                      zoom_start=20)  # Создаем основную карту
    folium.Marker(location=[latitude, longitude], zoom_start=20, popup=name, icon=folium.Icon(
        color='green')).add_to(city)  # На карте отмечаем название и иконку
    newpath = f'webapp/static/{name}'
    street_place = f'{name}/{name}.html'
    place_photo1 = f'{name}/{name}.jpg'
    place_photo2 = f'{name}/{name}1.jpg'
    place_photo3 = f'{name}/{name}2.jpg'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # Сохраняем карту.
        map = city.save(f'webapp/static/{name}/{name}.html')
    else:
        flash('Такое заведение есть!')
    return render_template('restaurant/detail.html', restaurant=restaurant, map=street_place, 
    photo1=place_photo1, photo2=place_photo2, photo3=place_photo3,)