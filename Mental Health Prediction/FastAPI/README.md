# Mental Health Prediction API

A Machine Learning project that predicts mental health outcomes based on lifestyle, social media usage, academic information, and stress-related features.

The trained Machine Learning model is integrated with **FastAPI** to provide predictions through a REST API.

## 🚀 Features

* Machine Learning model for mental health prediction
* FastAPI REST API
* Pydantic data validation
* Scikit-learn Pipeline for preprocessing and prediction
* Automatic categorical encoding and numerical preprocessing
* Interactive API documentation with Swagger UI
* Model saved using Joblib
* JSON-based prediction requests and responses

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* FastAPI
* Uvicorn
* Pydantic

## 📁 Project Structure

```text
Mental Health Prediction/
│
└── FastAPI/
    │
    ├── app/
    │   ├── main.py
    │   ├── schemas.py
    │   ├── prediction.py
    │   ├── model_loader.py
    │   │
    │   └── models/
    │       └── Mental_Health_Model.pkl
    │
    ├── venv/
    │
    └── requirements.txt
```

## ⚙️ Machine Learning Pipeline

The project uses a Scikit-learn Pipeline to combine preprocessing and the trained model.

The Pipeline handles preprocessing automatically before making a prediction.

Conceptually:

```text
Input Data
    ↓
Pandas DataFrame
    ↓
Preprocessing Pipeline
    ├── Numerical preprocessing
    └── Categorical encoding
    ↓
Machine Learning Model
    ↓
Prediction
```

This means the FastAPI application does not need to manually encode categorical variables or separately scale numerical features.

## 📊 Input Features

The API accepts the following features:

| Feature                 | Type    | Example       |
| ----------------------- | ------- | ------------- |
| Age                     | Integer | 21            |
| Gender                  | String  | Male          |
| Country                 | String  | Nepal         |
| Academic_Level          | String  | Undergraduate |
| Most_Used_Platform      | String  | Instagram     |
| Purpose_Of_Use          | String  | Entertainment |
| Avg_Daily_Usage_Hours   | Float   | 5.5           |
| Daily_Unlocks           | Integer | 20            |
| Study_Hours             | Float   | 3.0           |
| Physical_Activity_Hours | Float   | 1.5           |
| Sleep_Hours_Per_Night   | Float   | 7.0           |
| Stress_Level            | String  | High          |

## 📥 Example Request

Send a `POST` request to:

```text
/predict
```

Example JSON:

```json
{
    "Age": 21,
    "Gender": "Male",
    "Country": "Nepal",
    "Academic_Level": "Undergraduate",
    "Most_Used_Platform": "Instagram",
    "Purpose_Of_Use": "Entertainment",
    "Avg_Daily_Usage_Hours": 5.5,
    "Daily_Unlocks": 20,
    "Study_Hours": 3.0,
    "Physical_Activity_Hours": 1.5,
    "Sleep_Hours_Per_Night": 7.0,
    "Stress_Level": "High"
}
```

## 📤 Example Response

```json
{
    "prediction": 1
}
```

The exact prediction depends on the target variable and the trained Machine Learning model.

## 🔄 Prediction Flow

```text
Client
  │
  │ JSON Request
  ↓
FastAPI
  │
  ↓
Pydantic Validation
  │
  ↓
Pandas DataFrame
  │
  ↓
Saved ML Pipeline
  │
  ├── Preprocessing
  │
  └── Model Prediction
  │
  ↓
Python Value
  │
  ↓
JSON Response
```

## 🎯 Learning Objectives

This project was built to practice:

* Machine Learning model training
* Feature preprocessing
* Scikit-learn Pipelines
* Model serialization with Joblib
* FastAPI
* Pydantic validation
* REST APIs
* Connecting an ML model to an API
* JSON request/response handling
* Deploying Machine Learning models

## 🔮 Future Improvements

* Add a frontend application
* Add model performance metrics
* Add Docker support
* Deploy the API to a cloud platform
* Add automated testing
* Add logging and error handling
* Add model versioning

## 👨‍💻 Author

**Milan Rai**

AI & ML Learner | Python | Java | JavaScript | TypeScript
