from flask import Flask, render_template

from webapp.model import db, Place

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route("/")
    def index():
        title = "Рестораны Санкт-Петербурга"
        name = db.session.execute(db.select(Place)).scalars()
        return render_template('index.html',title=title, name=name)
    
    return app