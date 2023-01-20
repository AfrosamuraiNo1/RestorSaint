from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.restaurants.views import blueprint as restaurants_blueprint
from webapp.db import db
from webapp.user.models import User



def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(restaurants_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

app = create_app()

from webapp.admin.routes import admin_bp
app.register_blueprint(admin_bp, url_prefix="/admin")

from webapp.user.routes import users_bp
app.register_blueprint(users_bp, url_prefix="/user") 