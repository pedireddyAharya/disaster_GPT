import os
import joblib
import numpy as np
import pandas as pd

# Base directory of project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct relative paths
MODEL_PATH = os.path.join(BASE_DIR, "model", "earthquake_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "earthquake_encoder.pkl")

# Load model & encoder
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def predict_earthquake(magnitude, depth, latitude, longitude):
    data = pd.DataFrame([{
        "magnitude": magnitude,
        "depth": depth,
        "latitude": latitude,
        "longitude": longitude
    }])

    pred = model.predict(data)[0]
    risk = encoder.inverse_transform([pred])[0]
    return risk
