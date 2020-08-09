from flask import Flask

application = Flask(__name__)


@application.route("/")
def home():
    status = dict()
    status["code"] = "This is great"
    return status


if __name__ == "__main__":
    application.run()