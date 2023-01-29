from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp.db import db

from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

from webapp.user.routes import users_bp


@users_bp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('restaurants.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@users_bp.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('restaurants.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('users_blueprint.login'))


@users_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('restaurants.index'))


@users_bp.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('restaurants.index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template('user/registration.html', page_title=title, form=form)


@users_bp.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('users_blueprint.login'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('users_blueprint.register'))
