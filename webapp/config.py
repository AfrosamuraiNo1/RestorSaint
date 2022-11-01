import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATA_CSV1 = os.path.join(basedir, 'data_csv', 'address.csv')
DATA_CSV2 = os.path.join(basedir, 'data_csv', 'cards.csv')

SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')