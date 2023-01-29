from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime
from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hashed = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50))
    registered_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, username: str, role: str, password_plaintext: str, email: str):
        """
        Создайте новый пользовательский объект, используя адрес электронной почты и
        введите текстовый пароль с помощью Werkzeug.Безопасность.

        Create a new User object using the email address and hashing the
        plaintext password using Werkzeug.Security.
        """
        self.username = username
        self.role = role
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)
        self.registered_on = datetime.now()

    def is_password_correct(self, password_plaintext: str):
        return check_password_hash(self.password_hashed, password_plaintext)

    def set_password(self, password_plaintext: str):
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext):
        return generate_password_hash(password_plaintext)

    @property
    def is_authenticated(self):
        """Return True if the user has been successfully registered."""
        return True

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the user ID as a unicode string (`str`)."""
        return str(self.id)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def set_password_hashed(self, password_hashed):
        self.password_hashed = generate_password_hash(password_hashed)

    def check_password_hashed(self, password_hashed):
        return check_password_hash(self.password_hashed, password_hashed)

    def __repr__(self):
        return '<User {}>'.format(self.username)
