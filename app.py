import os
import requests
import operator
import re
from flask import Flask, render_template, request
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

@app.route('/addDevice', methods=['GET','POST'])
def addDevice():
    print 'posting now..'
    errors = []
    if request.method == 'POST':
        print 'in here'
        device = Device(request.form['imei'], request.form['deviceName'], request.form['serial'], request.form['sim'], request.form['realm'])
        db.session.add(device)
        db.session.commit()
    return render_template('new.html')
    
@app.route('/', methods=['GET'])    
def getDevices():
    errors = []
    print 'retrieving devices'
    return render_template('index.html', devices = db.session.query(Device).all())
    
@app.route('/devices/<int:device_id>', methods=['GET'])    
def getDevice(device_id):
    print 'retrieving a device'
    devices = db.session.query(Device).get(device_id)
    print devices.imei
    return render_template('index.html', device = db.session.query(Device).get(device_id))
    
if __name__ == '__main__':
    app.run()