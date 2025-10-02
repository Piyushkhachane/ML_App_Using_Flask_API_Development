from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

app = Flask(__name__)

MODEL_FILE = "model.pkl"

# Features (all except Outcome)
FEATURE_COLS = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

TARGET_COL = "Outcome"

# Train endpoint
@app.route('/train', methods=['POST'])
def train():
    file = request.files['file']
    df = pd.read_csv(file)

    X = df[FEATURE_COLS]
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    with open(MODEL_FILE, 'wb') as f:
        pickle.dump(model, f)

    accuracy = model.score(X_test, y_test)
    return jsonify({"message": "Model trained successfully!", "accuracy": accuracy})

# Test endpoint
@app.route('/test', methods=['POST'])
def test():
    if not os.path.exists(MODEL_FILE):
        return jsonify({"error": "Model not trained yet!"})

    file = request.files['file']
    df = pd.read_csv(file)

    X_test = df[FEATURE_COLS]
    y_test = df[TARGET_COL]

    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)
    accuracy = (y_pred == y_test).mean()

    return jsonify({"accuracy": accuracy})

# Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if not os.path.exists(MODEL_FILE):
        return jsonify({"error": "Model not trained yet!"})

    data = request.get_json()
    df = pd.DataFrame([data])

    X = df[FEATURE_COLS]

    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)

    pred = model.predict(X)[0]
    result = "Diabetic" if pred == 1 else "Not Diabetic"

    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
