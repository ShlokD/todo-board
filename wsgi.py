import os
import pymongo
from flask import Flask

application = Flask(__name__)

def get_collection():
    conn = pymongo.MongoClient('mongodb://' + os.environ['MONGODB_SERVICE_HOST'] + ':' + os.environ['MONGODB_SERVICE_PORT'] + '/sampledb')
    for db in conn.list_database_names():
        print("database", db);
        print("collections", conn[db].collection_names())
    
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