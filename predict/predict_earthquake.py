import joblib
import pandas as pd

model = joblib.load("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/model/earthquake_model.pkl")
encoder = joblib.load("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/model/earthquake_encoder.pkl")

def predict_earthquake(magnitude, depth, latitude, longitude, tsunami):
    data = pd.DataFrame([{
        "magnitude": magnitude,
        "depth": depth,
        "latitude": latitude,
        "longitude": longitude,
        "tsunami": tsunami
    }])

    pred = model.predict(data)
    return encoder.inverse_transform(pred)[0]
