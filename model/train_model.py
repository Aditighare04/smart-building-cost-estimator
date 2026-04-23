import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

# Load dataset
data_path = os.path.join("..", "data", "building_data.csv")
data = pd.read_csv(data_path)

# Features & target
X = data.drop("cost", axis=1)
y = data["cost"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
score = r2_score(y_test, y_pred)
print(f"Model Accuracy (R2 Score): {score:.2f}")

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved successfully!")
