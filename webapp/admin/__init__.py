from flask_admin import expose, Admin
from webapp import app
from webapp.db import db
from webapp.user.models import User
from webapp.restaurants.models import Place
from flask_admin.contrib.sqla import ModelView
import flask_admin

# Панель администратора. Сделана с помощью Flask-Admin.
# Admin panel. Made using Flask-Admin.


class MyHomeView(flask_admin.AdminIndexView):
    @expose('/')
    def index(self):
        title = 'Панель управления'
        return self.render('admin/index.html', title=title)


admin = Admin(app, index_view=MyHomeView(),
              name="Админка", template_mode="bootstrap3")
admin.add_view(ModelView(Place, db.session, name='Ресторан'))
admin.add_view(ModelView(User, db.session, name='Пользователи'))
