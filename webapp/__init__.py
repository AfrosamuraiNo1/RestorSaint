from flask import Flask, render_template
from webapp.model import Place, db
#from utils_csv import data_address

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Рeсторан Санкт-Петербурга"
        weather = 'бывает'
        news = Place.query.order_by(Place.title.desc()).all()
        return render_template('index.html',page_title=title, weather=weather, news_list=news)
    
    return app         