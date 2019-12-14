import pyrebase
import json

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


def stream_handler(message):
    try:
        print(message)
        meterId = message["path"].split("/")[1]
        print("meterid: ", meterId)
        changedMeterInMeters = db.child("meters").child(meterId).get().val()
        clusterId = changedMeterInMeters["clusterId"]
        print("Its cluster: ", clusterId)
        #print("Cluster values: ", db.child("clusters").child(clusterId).get().val())
        allMeters = db.child("meters").get().val()
        allMeters_values = allMeters.values()
        avgPowerConsumed = sum([i["powerConsumed"] for i in allMeters_values])/len(allMeters_values)
        avgPowerGenerated = sum([i["powerGenerated"] for i in allMeters_values]) / len(allMeters_values)
        #print("avgPowerConsumed: ",avgPowerConsumed," avgPowerGenerated",avgPowerGenerated)
        print("Changing: (The changed meter in cluster) ",db.child("clusters").child(clusterId).child("smartMeters").child(meterId).set(changedMeterInMeters))
        print("Changing: (The changed aggregatedPowerGenerated) ",db.child("clusters").child(clusterId).update({"aggregratedPowerGenerated":avgPowerGenerated,"aggregatedPowerConsumed":avgPowerConsumed}))
    except Exception as e:
        print('At Exception ', e)
        pass

my_stream = db.child("meters").stream(stream_handler)
