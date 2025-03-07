import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict(np.array(data).reshape(1, -1))
    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
