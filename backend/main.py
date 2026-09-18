import pickle
from pathlib import Path

import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import RootModel, field_validator
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# ==========================================
# CORS Middleware
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# Input Validation Classes
# ==========================================

class DiabetesInput(RootModel[list[float]]):

    @field_validator("root")
    @classmethod
    def validate_data(cls, data):
        if len(data) != 8:
            raise ValueError(
                "Diabetes prediction requires exactly 8 features."
            )
        return data


class HeartInput(RootModel[list[float]]):

    @field_validator("root")
    @classmethod
    def validate_data(cls, data):
        if len(data) != 13:
            raise ValueError(
                "Heart disease prediction requires exactly 13 features."
            )
        return data


class ParkinsonsInput(RootModel[list[float]]):

    @field_validator("root")
    @classmethod
    def validate_data(cls, data):
        if len(data) != 22:
            raise ValueError(
                "Parkinsons prediction requires exactly 22 features."
            )
        return data


# ==========================================
# Load Trained Models
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"


diabetes_model = pickle.load(
    open(MODEL_DIR / "diabetes_model.sav", "rb")
)


heart_disease_model = pickle.load(
    open(MODEL_DIR / "heart_disease_model.sav", "rb")
)


parkinsons_model = pickle.load(
    open(MODEL_DIR / "parkinsons_model.sav", "rb")
)


# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Multi Disease Prediction API is running"
    }


# ==========================================
# Diabetes Prediction
# ==========================================

@app.post("/prediction/diabetes")
def predict_diabetes(data: DiabetesInput):

    try:
        input_data = np.asarray(data.root)
        input_data = input_data.reshape(1, -1)

        prediction = diabetes_model.predict(input_data)

        if prediction[0] == 1:
            result = "Diabetic"
        else:
            result = "Not Diabetic"

        return {
            "prediction": int(prediction[0]),
            "result": result
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Diabetes prediction failed. Please try again."
        )


# ==========================================
# Heart Disease Prediction
# ==========================================

@app.post("/prediction/heart")
def predict_heart(data: HeartInput):

    try:
        input_data = np.asarray(data.root)
        input_data = input_data.reshape(1, -1)

        prediction = heart_disease_model.predict(input_data)

        if prediction[0] == 1:
            result = "Heart Disease"
        else:
            result = "Not Heart Disease"

        return {
            "prediction": int(prediction[0]),
            "result": result
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Heart disease prediction failed. Please try again."
        )


# ==========================================
# Parkinson's Prediction
# ==========================================

@app.post("/prediction/parkinsons")
def predict_parkinsons(data: ParkinsonsInput):

    try:
        input_data = np.asarray(data.root)
        input_data = input_data.reshape(1, -1)

        prediction = parkinsons_model.predict(input_data)

        if prediction[0] == 1:
            result = "Parkinsons Disease"
        else:
            result = "Not Parkinsons Disease"

        return {
            "prediction": int(prediction[0]),
            "result": result
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Parkinsons prediction failed. Please try again."
        )
