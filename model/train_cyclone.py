import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/data/cyclone_dataset.csv")

# Features & target
X = data.drop("Cyclone", axis=1)
y = data["Cyclone"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model/cyclone_model.pkl")

print("✅ Cyclone model trained successfully")
