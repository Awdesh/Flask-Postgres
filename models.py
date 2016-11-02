from app import db
from sqlalchemy.dialects.postgresql import JSON

class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    imei = db.Column(db.Integer)
    name = db.Column(db.String)

    def __init__(self, imei, name):
        self.imei = imei
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)