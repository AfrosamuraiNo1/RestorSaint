import pytest

from webapp import app, db
from webapp.user.models import User


# --------
# Fixtures
# --------


# Фикстура базы данных
@pytest.fixture(scope='module')
def new_user():
    user = User(username='patkennedy', password_plaintext='FlaskIsAwesome',role='user', email='patkennedy79@gmail.com')
    return user

# Фикстура фласк тест клиента.
@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    app.testing = True
    with app.test_client() as client:
        # Establish an application context
        with app.app_context():
            yield client # this is where the testing happens!

# Фикстура для базы данны создает двух новых юзеров

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(username='patkennedy', password_plaintext='FlaskIsAwesome' ,role='user', email='patkennedy79@gmail.com')
    user2 = User(username='kenne',  password_plaintext='PaSsWoRd',role='user', email='kennedyfamilyrecipes@gmail.com')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

# Фикстура создает нового юзера через тест клиента.

@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(username='patkennedy', password_plaintext='FlaskIsAwesome' ,role='user', email='patkennedy79@gmail.com'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
