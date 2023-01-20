from webapp import create_app
from webapp.utils_csv import base_restaurant

app = create_app()
with app.app_context():
    base_restaurant()