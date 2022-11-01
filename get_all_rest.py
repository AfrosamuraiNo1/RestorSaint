from webapp import create_app
from webapp.utils_csv import data_base

app = create_app()
with app.app_context():
    data_base()