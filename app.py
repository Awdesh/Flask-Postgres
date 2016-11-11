import os
import requests
import operator
import re
from flask import Flask, render_template, request, flash, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from collections import Counter

from rq import Queue
from rq.job import Job
from worker import conn


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# binding the db instance to the flask app
db = SQLAlchemy(app)

from models import Device
from models import Patient
from models import Sim

@app.route('/addDevice', methods=['GET','POST'])
def addDevice():
    print 'posting now..'
    errors = []
    if request.method == 'POST':
        print 'in here'
        device = Device(int(request.form['imei']), request.form['deviceName'], int(request.form['serial']), int(request.form['sim']), request.form['realm'])
        db.session.add(device)
        db.session.commit()
        flash('you have successfully created item.')
    return render_template('new.html')
    
@app.route('/addPatient', methods=['GET','POST'])
def addPatient():
    print 'posting now..'
    errors = []
    if request.method == 'POST':
        print 'in here'
        patient = Patient((request.form['firstName']), request.form['lastName'], (request.form['title']), (request.form['gender']), request.form['address1'])
        db.session.add(patient)
        db.session.commit()
        flash('you have successfully created item.')
    return render_template('newpatient.html')
    
@app.route('/', methods=['GET'])    
def getDevices():
    errors = []
    print 'retrieving devices'
    devices = db.session.query(Device).all()
    if len(devices) < 0:
        flash('There are no items yet.')
        return
    else:
        flash('Below are the devices.')
        return render_template('index.html', devices = devices)
    
@app.route('/devices/<int:device_id>', methods=['GET'])    
def getDevice(device_id):
    print 'retrieving a device'
    print device_id
    device = db.session.query(Device).get(device_id)
    if device is None:
        flash('There is no device with this Id.')
    print device.imei
    return render_template('index.html', device = db.session.query(Device).get(device_id))
    
@app.route('/devices/<string:realm>', methods=['GET'])    
def getDeviceByRealm(realm):
    print 'retrieving a device from imei'
    device = Device.query.filter_by(realm=realm).first_or_404()
    return render_template('index.html', device = device)
    
@app.route('/getPatients', methods=['GET'])    
def getPatients():
    errors = []
    print 'retrieving patients'
    return render_template('patient.html', patients = db.session.query(Patient).all())
    
if __name__ == '__main__':
    app.run()