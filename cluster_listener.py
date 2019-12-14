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
        if len(message["path"].split("/"))==2:
            clusterId = message["path"].split("/")[1]
            print("clusterId: ",clusterId)
            changedClusterInClusters = db.child("clusters").child(clusterId).get().val()
            substationId = changedClusterInClusters["substationId"]
            print(substationId)
            allClusters = db.child("clusters").get().val()
            allClusters_values = allClusters.values()
            avgPowerConsumed = sum([i["aggregatedPowerConsumed"] for i in allClusters_values]) / len(allClusters_values)
            avgPowerGenerated = sum([i["aggregratedPowerGenerated"] for i in allClusters_values]) / len(allClusters_values)
            print("avgPowerConsumed: ", avgPowerConsumed, " avgPowerGenerated", avgPowerGenerated)
            print("Changing: (The changed meter in cluster) ",
                  db.child("substations").child(substationId).child("clusterHeads").child(clusterId).set(changedClusterInClusters))
            print("Changing: (The changed aggregatedPowerGenerated) ",
                  db.child("substations").child(substationId).update({"aggregratedPowerGenerated": avgPowerGenerated, "aggregatedPowerConsumed": avgPowerConsumed}))

    except Exception as e:
        print('At Exception ', e)
        pass

my_stream = db.child("clusters").stream(stream_handler)