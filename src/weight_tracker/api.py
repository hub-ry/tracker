from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
FILE = "weight.txt"

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
    app.run(host="0.0.0.0")
