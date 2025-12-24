import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load cleaned dataset
data = pd.read_csv("C:/Users/ahary/OneDrive/Desktop/disaster_GPT/data/flood_data.csv")

# Select features and target
X = data[['Slope', 'TWI', 'FA', 'Drainage', 'Rainfall']]
y = data['risk']

# Encode target labels (Low, Moderate, High, Very_High)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "flood_model.pkl")
joblib.dump(encoder, "risk_encoder.pkl")

print("✅ Flood risk model trained successfully!")
