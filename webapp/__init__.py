from flask import Flask, render_template

from webapp.model import db, Place


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Рестораны Санкт-Петербурга"
        name = Place.query.all()
        return render_template('index.html', title=title, name_list=name)
    
    return app


app = Flask(__name__)

@app.route('/map')
def map():
    return render_template('index.html', map='restaurants-spb.html')	


if __name__ == '__main__':
    app.run(debug=True)    