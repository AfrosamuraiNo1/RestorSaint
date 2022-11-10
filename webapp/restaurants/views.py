from flask import render_template
from webapp.restaurants.models import Place
from flask import Blueprint
from flask_login import current_user

blueprint = Blueprint('restaurants', __name__)

@blueprint.route("/")
def index():
    title = "Рестораны Санкт-Петербурга"
    name = Place.query.all()
    return render_template('restaurant/index.html',title=title, name_list=name)