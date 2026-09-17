from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return{
        "Message": "Meantal Health Score Prediction Of the Student"
    }

