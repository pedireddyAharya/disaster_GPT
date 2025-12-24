import joblib
import pandas as pd

# Load trained cyclone model
model = joblib.load("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/model/cyclone_model.pkl")

def predict_cyclone(inputs: dict):
    """
    Build input DataFrame using the EXACT feature order
    used during training.
    """

    # Get correct feature order from the trained model
    feature_order = model.feature_names_in_

    # Build row in the SAME order
    row = [inputs.get(feature, 0) for feature in feature_order]

    df = pd.DataFrame([row], columns=feature_order)

    pred = model.predict(df)[0]
    return "High" if pred == 1 else "Low"
