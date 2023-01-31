from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from webapp.user.models import User

"""
Для того чтобы с нуля не писать свои проверки паролей, почты и т д мы используем Wtforms.
Также мы используем render_kw={"class": "form-control"} для внешнего вида.

In order not to write our own password checks, mail, etc. from scratch, we use Wtforms.
We also use render_kw={"class": "form-control"} for the appearance.
"""


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
                           DataRequired()], render_kw={"class": "form-control"})
    password_plaintext = PasswordField('Пароль', validators=[DataRequired()], render_kw={
                             "class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={
                               "class": "form-check-input"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
                           DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "class": "form-control"})
    password_plaintext = PasswordField('Пароль', validators=[DataRequired()], render_kw={
                             "class": "form-control"})
    password_plaintext2 = PasswordField('Повторите пароль', validators=[
                              DataRequired(), EqualTo('password_plaintext')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError(
                'Пользователь с таким именем уже зарегистрирован')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError(
                'Пользователь с такой электронной почтой уже зарегистрирован')
