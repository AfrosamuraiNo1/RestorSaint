from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.db import db
from webapp.user.models import User
import os


def create_app(config_filename=None):
    app = Flask(__name__, static_folder="static")
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    from webapp.restaurants.views import blueprint as restaurants_blueprint
    app.register_blueprint(restaurants_blueprint, url_prefix="/")
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app

app = create_app()

from webapp.admin.routes import admin_bp
app.register_blueprint(admin_bp, url_prefix="/admin")

from webapp.user.routes import users_bp
app.register_blueprint(users_bp, url_prefix="/user") 