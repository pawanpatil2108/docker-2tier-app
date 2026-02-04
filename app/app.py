from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Docker 2-Tier Application is Running"

app.run(host="0.0.0.0", port=5000)

