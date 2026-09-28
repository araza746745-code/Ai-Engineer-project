from fastapi import FastAPI, HTTPException
import numpy as np
import joblib

app = FastAPI()

# Load trained model
model = joblib.load("sales_model.pkl")


@app.get("/")
def home():
    return {
        "message": "Sales Prediction API is running"
    }


@app.post("/predict")
def predict(features: list[float]):

    # Model needs exactly 18 features
    if len(features) != 18:
        raise HTTPException(
            status_code=400,
            detail=f"Expected 18 features, but received {len(features)}"
        )

    # Convert input into model format
    data = np.array(features).reshape(1, -1)

    # Prediction
    prediction = model.predict(data)

    return {
        "predicted_gross_amount": float(prediction[0])
    }