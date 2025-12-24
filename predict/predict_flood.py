import joblib
import numpy as np

# Load trained model and encoder
model = joblib.load("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/model/flood_model.pkl")
encoder = joblib.load("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/model/risk_encoder.pkl")

def predict_flood_risk(slope, twi, fa, drainage, rainfall):
    input_data = np.array([[slope, twi, fa, drainage, rainfall]])
    prediction = model.predict(input_data)
    risk = encoder.inverse_transform(prediction)
    return risk[0]

# Test the prediction
if __name__ == "__main__":
    result = predict_flood_risk(
        slope=60,
        twi=-4.1,
        fa=150,
        drainage=235,
        rainfall=120
    )
    print("🌊 Predicted Flood Risk:", result)
