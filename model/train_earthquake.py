import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/data/earthquake_data.csv")

# Features & target
X = data[["magnitude", "depth", "latitude", "longitude", "tsunami"]]
y = data["alert"]

# Encode target
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y_encoded)

# Save model
joblib.dump(model, "model/earthquake_model.pkl")
joblib.dump(encoder, "model/earthquake_encoder.pkl")

print("✅ Earthquake model trained successfully")
