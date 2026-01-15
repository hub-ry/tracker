from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
FILE = "weight.txt"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Weight Tracker API",
        "version": "2.0",
        "endpoints": {
            "add_weight": {"method": "POST", "url": "/add_weight", "description": "Add a new weight entry"},
            "get_weights": {"method": "GET", "url": "/get_weights", "description": "Get all weight entries"}
        }
    })

#define URL endpoint, path to add_weight, POST is to send data
@app.route("/add_weight", methods=["POST"]) 
def add_weight():
  data = request.get_json()

  weight = data.get("weight")
  if weight is None:
    # extract the weight from the JSON
    # if the weight in None; HTTP 400 is bad request
    return jsonify({"status": "error", "message": "No weight provided"}), 400
  today = datetime.today().strftime("%Y-%m-%d")
  with open(FILE, "a") as f:
    f.write(f"{today}, {weight}\n")
  return jsonify({"status": "ok", "weight": weight, "date": today})


# for laptop to PULL the weights
@app.route("/get_weights", methods=["GET"])
def get_weights():
    if not os.path.exists(FILE):
      return jsonify({"weights": []})
    with open(FILE, "r") as f:
      lines = f.readlines()
      weights = [{"date": line.split(",")[0].strip(), "weight": line.split(",")[1].strip()} for line in lines]
    return jsonify({"weights": weights})


if __name__ == "__main__":
    app.run(host="100.89.197.38", port=5000)
