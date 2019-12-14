import pyrebase
import time
import json
import random

testing_config = json.load(open('config.json', 'r'))
#testing_config = json.load(open('testing_firebase_config.json', 'r'))

config = {
    "apiKey": testing_config['apiKey'],
    "authDomain": testing_config['authDomain'],
    "databaseURL": testing_config['databaseURL'],
    "storageBucket": testing_config['storageBucket']
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

meterId = "-Lw0rhVeuO0Tdp22jItm"

while True:
    db.child("meters").child(meterId).update({"powerConsumed":random.randint(5,10)})
    time.sleep(7)