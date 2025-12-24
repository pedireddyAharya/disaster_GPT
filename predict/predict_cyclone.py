import os
import joblib
import pandas as pd

# Base directory of project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct relative paths
MODEL_PATH = os.path.join(BASE_DIR, "model", "cyclone_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "cyclone_encoder.pkl")

# Load model and encoder
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def predict_cyclone(
    Sea_Surface_Temperature,
    Atmospheric_Pressure,
    Humidity,
    Wind_Shear,
    Vorticity,
    Latitude,
    Ocean_Depth,
    Proximity_to_Coastline,
    Pre_existing_Disturbance
):
    df = pd.DataFrame([{
        "Sea_Surface_Temperature": Sea_Surface_Temperature,
        "Atmospheric_Pressure": Atmospheric_Pressure,
        "Humidity": Humidity,
        "Wind_Shear": Wind_Shear,
        "Vorticity": Vorticity,
        "Latitude": Latitude,
        "Ocean_Depth": Ocean_Depth,
        "Proximity_to_Coastline": Proximity_to_Coastline,
        "Pre_existing_Disturbance": Pre_existing_Disturbance
    }])

    pred = model.predict(df)[0]
    risk = encoder.inverse_transform([pred])[0]
    return risk
