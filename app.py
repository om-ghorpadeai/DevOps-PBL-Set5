from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps PBL Set 5 - Docker Application Running Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
