from webapp.db import db

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    info = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    description = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f'Place: {self.name}{self.info}{self.address}{self.description}'