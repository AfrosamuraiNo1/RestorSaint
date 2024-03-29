from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user

# Декоратор проверки пользователя
# User verification decorator


def admin_required(func):
    @wraps(func)  # Сохраняет имя и опсиание функции __name__ и __doc__
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash('Эта страница доступна только админам')
            return redirect(url_for('restaurant.index'))
        return func(*args, **kwargs)
    return decorated_view
