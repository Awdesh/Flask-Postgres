from app import db
from sqlalchemy.dialects.postgresql import JSON

class Device(db.Model):
    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    imei = db.Column(db.BigInteger)
    name = db.Column(db.String)
    serial = db.Column(db.BigInteger)
    sim = db.Column(db.BigInteger)
    realm = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, imei, name, serial, sim, realm):
        self.imei = imei
        self.name = name
        self.serial = serial
        self.sim = sim
        self.realm = realm

    def __repr__(self):
        return '<id {}>'.format(self.id)
        
class Patient(db.Model):
    __tablename__ = 'patient'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    title = db.Column(db.String)
    gender = db.Column(db.String)
    height = db.Column(db.String)
    address1 = db.Column(db.String)
    address2 = db.Column(db.String)
    city = db.Column(db.String)
    
    def __init__(self, first_name, last_name, title, gender, address1):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.gender = gender
        self.address1 = address1
        # self.address2 = address2
        # self.city = city

    def __repr__(self):
        return '<id {}>'.format(self.id)
        
class Sim(db.Model):
    __tablename = 'sim'
    
    id = db.Column(db.Integer, primary_key=True)
    imsi = db.Column(db.String)
    caller_id_number = db.Column(db.String)
    iccid = db.Column(db.String)
    network_operator = db.Column(db.String)
    
    def __init__(self, imsi, caller_id_number, iccid, network_operator):
        self.imsi = imsi
        self.caller_id_number = caller_id_number
        self.iccid = iccid
        self.network_operator = network_operator

    def __repr__(self):
        return '<id {}>'.format(self.id)