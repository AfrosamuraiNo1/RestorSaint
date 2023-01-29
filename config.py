import os
from webapp.config import BASEDIR
from datetime import timedelta

REMEMBER_COOKIE_DURATION = timedelta(days=5)

# Determine the folder of the top-level directory of this project

DATA_CSV1 = os.path.join(BASEDIR, 'data_csv', 'address.csv')
DATA_CSV2 = os.path.join(BASEDIR, 'data_csv', 'cards.csv')

class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default="vrevprembs';bsrbs[pbpmor2134255340=fdkpsbmopvm-0stu4i;oa")
    # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
    # update the URI to the postgres database to use the supported 'postgresql://' scheme
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, '..', 'webapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',default='sqlite:///' + os.path.join(BASEDIR, '..', 'test.db'))
    WTF_CSRF_ENABLED = False