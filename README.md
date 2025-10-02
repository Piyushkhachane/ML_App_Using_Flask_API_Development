# ML App Using Flask API Development
# 🩺 Diabetes Prediction API
A Flask REST API to train, test and predict diabetes using a **Random Forest model**.  
This repo contains the backend, model serialization, and examples to test via Postman or curl.

---

## 🚀 Features
- Train model by uploading a CSV via `/train` (saves `model.pkl`).  
- Evaluate model with a test CSV via `/test`.  
- Predict diabetes status with JSON input via `/predict`.  
- Lightweight and reproducible backend with clear ML workflow.  

---

## 📂 Repository structure
```
diabetes_project/
├─ app.py              # Flask app with /train, /test, /predict
├─ requirements.txt    # Python dependencies
├─ README.md           # Project documentation
├─ dataset/            # (optional) store CSVs for testing
└─ model.pkl           # generated after training
```

---

## 🛠️ Requirements
- Python 3.10+  
- Flask  
- pandas  
- scikit-learn  
- numpy  

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ⚡ Quick start (VS Code / Terminal)

1. Open project folder in VS Code.  
2. Create & activate a venv:  
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
   👉 Visit `http://127.0.0.1:5000` (all endpoints are **POST**).

---

## 📌 API Endpoints

### 🔹 `/train` — Train model
- **Method**: POST  
- **Body type**: `form-data` → key = `file` (type = File)  

Example (Postman): choose file `diabetes.csv` as the file field.  

✅ Response:
```json
{
  "message": "Model trained successfully!",
  "accuracy": 0.81
}
```

---

### 🔹 `/test` — Evaluate model
- **Method**: POST  
- **Body type**: `form-data` → key = `file` (type = File)  

✅ Response:
```json
{
  "accuracy": 0.78
}
```

---

### 🔹 `/predict` — Predict diabetes
- **Method**: POST  
- **Body type**: raw (application/json)  

Example JSON:
```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 85,
  "BMI": 25.3,
  "DiabetesPedigreeFunction": 0.45,
  "Age": 33
}
```

✅ Example response:
```json
{
  "prediction": "Not Diabetic"
}
```

---

## 🖥️ curl examples

**Train:**
```bash
curl -X POST "http://127.0.0.1:5000/train" -F "file=@/path/to/diabetes.csv"
```

**Predict:**
```bash
curl -X POST "http://127.0.0.1:5000/predict"   -H "Content-Type: application/json"   -d '{"Pregnancies":2,"Glucose":120,"BloodPressure":70,"SkinThickness":20,"Insulin":85,"BMI":25.3,"DiabetesPedigreeFunction":0.45,"Age":33}'
```

---

## 📬 Postman quick tips
- For file endpoints use **Body → form-data**. Choose type **File** for the key `file`.  
- For `/predict`, use **Body → raw** and select **JSON**.  
- Create a Collection named **Diabetes API** with three saved requests: Train, Test, Predict.  

---

## 🧪 Model details
- **Algorithm**: RandomForestClassifier (n_estimators=100)  
- **Target**: `Outcome` column (0 = Not Diabetic, 1 = Diabetic)  
- **Features**:  
  - Pregnancies  
  - Glucose  
  - BloodPressure  
  - SkinThickness  
  - Insulin  
  - BMI  
  - DiabetesPedigreeFunction  
  - Age  

---

## ❗ Troubleshooting
- **Not Found error**: Ensure Flask is running (`python app.py`) and you use exact endpoints: `/train`, `/test`, `/predict`.  
- **Feature names mismatch**: Retrain the model (call `/train`) so `model.pkl` matches expected features. Use same column names/order as dataset.  
- **500 error (KeyError: 'file')**: In Postman, make sure Body is set to `form-data` and key is exactly `file`. 
