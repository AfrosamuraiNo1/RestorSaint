import os
from datetime import timedelta

REMEMBER_COOKIE_DURATION = timedelta(days=5)
        
basedir = os.path.abspath(os.path.dirname(__file__))

DATA_CSV1 = os.path.join(basedir, 'data_csv', 'address.csv')
DATA_CSV2 = os.path.join(basedir, 'data_csv', 'cards.csv')

SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = "vrevprembs';bsrbs[pbpmor2134255340=fdkpsbmopvm-0stu4i;oa"

SQLALCHEMY_TRACK_MODIFICATIONS = False