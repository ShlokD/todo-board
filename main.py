from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    status = dict()
    status["code"] = "This is great, too"
    return status


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=8080)