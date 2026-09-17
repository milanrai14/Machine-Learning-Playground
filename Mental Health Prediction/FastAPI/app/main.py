from fastapi import FastAPI, HTTPException
from schemas import HealthDetailRequest
from prediction import predict_mental_healh

app = FastAPI(
    title="Mental Health Prediction API",
    description="API for predicting mental health using Machine Learning",
    version="1.0.0"
)

@app.get("/")
def home():
    return{
        "Message": "Meantal Health Score Prediction Of the Student"
    }

@app.post('/predict')
def health_prediction(req: HealthDetailRequest):
    prediction = predict_mental_healh(req)

    return {
        'Prediction': prediction
    }