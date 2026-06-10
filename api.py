from flask import Flask, request, jsonify
import joblib
import numpy as np
from config import DISEASES

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    req = request.json
    disease = req["disease"]
    data = req["data"]

    # file-safe name
    file_name = disease.lower().replace(" ", "_")

    try:
        model = joblib.load(f"models/{file_name}_model.pkl")
        scaler = joblib.load(f"models/{file_name}_scaler.pkl")
        features = joblib.load(f"models/{file_name}_features.pkl")
    except:
        return {"error": "Model files not found"}, 404

    x = np.array(data).reshape(1, -1)
    x_scaled = scaler.transform(x)

    pred = model.predict(x_scaled)[0]
    prob = model.predict_proba(x_scaled)[0][1]

    return {
        "prediction": int(pred),
        "probability": float(prob)
    }

app.run(port=5000)
