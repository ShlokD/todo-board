import os
import pymongo
from flask import Flask

application = Flask(__name__)

def get_collection():
    for key in os.environ:
        print(key, ':', os.environ[key])
    
    conn = pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
    return conn["sampledb"]["samplecollection"]


@application.route("/")
def home():
    status = dict()
    status["code"] = "This is great"
    return status


@application.route("/post")
def post():
    collection = get_collection()
    data = { "message": "Om Namah Shivay"}
    inserted = collection.insert_one(data)
    return { id: inserted.inserted_id }


@application.route("/get-message")
def get_message():
    collection = get_collection()
    data = collection.find_one()
    return data


if __name__ == "__main__":
    application.run()