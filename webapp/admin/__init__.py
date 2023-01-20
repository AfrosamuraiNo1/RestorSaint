from flask_admin import expose, Admin
from webapp import app
from webapp.db import db
from webapp.user.models import User
from webapp.restaurants.models import Place
from flask_admin.contrib.sqla import ModelView
import flask_admin
from flask import redirect, url_for
from flask_login import logout_user

class MyHomeView(flask_admin.AdminIndexView):
    @expose('/')
    def index(self):
        title = 'Панель управления'
        return self.render('admin/index.html', title=title)

admin = Admin(app, index_view=MyHomeView(), name="Админка", template_mode="bootstrap3")
admin.add_view(ModelView(Place, db.session, name='Ресторан'))
admin.add_view(ModelView(User, db.session, name ='Пользователи'))

from flask_security import current_user
from flask_admin.menu import MenuLink
