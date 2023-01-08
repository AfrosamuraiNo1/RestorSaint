from webapp.db import db

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    info = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f'Place: {self.name}{self.info}{self.address}{self.description}{self.latitude}{self.longitude}'