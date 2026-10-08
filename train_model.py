import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Demo training data for the HealthGuard AI prototype
# This is synthetic data for a college project demonstration.

np.random.seed(42)

data = []
labels = []

for _ in range(1000):
    age = np.random.randint(18, 81)
    bmi = np.random.uniform(18, 40)
    heart_rate = np.random.randint(55, 111)
    systolic_bp = np.random.randint(90, 181)
    glucose = np.random.randint(70, 201)
    sleep = np.random.uniform(4, 10)
    exercise = np.random.randint(0, 8)

    # Synthetic demonstration rule for creating labels
    risk_score = 0

    if age >= 50:
        risk_score += 1

    if bmi >= 30:
        risk_score += 1

    if heart_rate >= 100:
        risk_score += 1

    if systolic_bp >= 140:
        risk_score += 1

    if glucose >= 140:
        risk_score += 1

    if sleep < 6:
        risk_score += 1

    if exercise < 2:
        risk_score += 1

    risk = 1 if risk_score >= 3 else 0

    data.append([
        age,
        bmi,
        heart_rate,
        systolic_bp,
        glucose,
        sleep,
        exercise
    ])

    labels.append(risk)

X = np.array(data)
y = np.array(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("HealthGuard AI Model Training Complete!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save the trained model
joblib.dump(model, "healthguard_model.pkl")

print("Model saved as healthguard_model.pkl")