import pandas as pd
from flask import Flask, request, jsonify
import joblib
import numpy as np
from body import sex, embarked, name

app = Flask(__name__)

clf = joblib.load("titanic_model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data["features"]

    sex(data)    
    embarked(data)
    name(data)

    X = pd.DataFrame.from_dict(features, orient="index").T
    predictions = clf.predict(X)

    prediction_map = {0: "Did not survive", 1: "Survived"}
    predictions = [prediction_map[p] for p in predictions]

    return jsonify({"predictions": predictions})


if __name__ == "__main__":
    app.run(debug=True)
