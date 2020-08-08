from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    status = dict()
    status["code"] = "OK"
    return status


if __name__ == "__main__":
    app.run()