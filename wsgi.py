import os
import pymongo
from flask import Flask

application = Flask(__name__)

def get_collection():
    conn = pymongo.MongoClient('mongodb://' + os.environ['MONGODB_SERVICE_HOST'] + ':' + os.environ['MONGODB_SERVICE_PORT'] + '/sampledb')
    for db in conn.list_database_names():
        print("database", db);
        print("collections", conn[db].collection_names())


@application.route("/")
def home():
    status = dict()
    status["code"] = "This is great, too"
    return status


@application.route("/post")
def post():
    get_collection()
    return { "message": "posting data..."}


@application.route("/get-message")
def get_message():
    get_collection()
    return {"message": "getting data..."}


if __name__ == "__main__":
    application.run()