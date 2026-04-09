import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

from utils.preprocessing import preprocess_data

# Load dataset
df = pd.read_csv('data/dataset.csv')

# Preprocess data
df = preprocess_data(df)

# Features and target
X = df[['area', 'floors', 'location', 'material', 'building_type']]
y = df['cost']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
score = model.score(X_test, y_test)
print(f"Model R² Score: {score}")

# Save model
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)