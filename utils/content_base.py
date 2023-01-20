from webapp.db import db
from webapp.restaurants.models import Place
from creater_map_city import geo_point
from webapp import create_app

app = create_app()

def content_filling():
    geo = geo_point()
    with app.app_context():
        for name, data in geo.items(): # В цикле заносит все данные в базу
            address = data['address']
            description = data['description']
            info = data['info']
            latitude=data['latitude']
            longitude=data['longitude']
            query = db.select(Place).filter_by(name=name)
            exists = db.session.execute(query).first()
            if not exists:
                new_place = Place(name=name, info=info, address=address, description=description, latitude=latitude,longitude=longitude)
                db.session.add(new_place)
                db.session.commit()
            else:
                db.session.commit()
        return 'well done'


def update_content_filling(): #Обновляет координаты
    geo = geo_point()
    with app.app_context():
        for name, data in geo.items():
            restaurant = Place.query.filter_by(name=name).first()
            new_latitude = data['latitude'] 
            new_longitude = data['longitude']
            if not name:
                print('Нет совподений по имени!')
            else:
                restaurant.latitude=new_latitude
                restaurant.longitude=new_longitude
                db.session.commit()

update_content_filling()