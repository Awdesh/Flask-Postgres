import os
import requests
import operator
import re
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from collections import Counter
from bs4 import BeautifulSoup

from rq import Queue
from rq.job import Job
from worker import conn


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# binding the db instance to the flask app
db = SQLAlchemy(app)

from models import Device

@app.route('/addDevice', methods=['GET', 'POST'])
def addDevice():
    print 'posting now..'
    errors = []
    try:
        device = Device(
            imei=1234566,
            name="dev_device",
            realm="dev",
            serial=12345,
            sim=3153454567
        )
        db.session.add(device)
        print device
        print device.id
        print device.name
        print device.sim
        db.session.commit()
    except:
        errors.append("Unable to add items to the database")
    return render_template('index.html')
    
@app.route('/getDevice', methods=['GET'])    
def getDevice():
    errors = []
    print 'retrieving a device'
    try:
        devices = db.session.query(Device).all()
        print len(devices)
    except:
        errors.append("Unable to retrieve items from the database")
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run()