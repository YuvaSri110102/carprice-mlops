from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("artifacts/model_pipeline.pkl")
app = FastAPI()

class CarFeatures(BaseModel):

    brand: str
    model: str
    vehicle_age: int
    km_driven: int
    seller_type: str
    fuel_type: str
    transmission_type: str
    mileage: float
    engine: int
    max_power: float
    seats: int

@app.get("/")
def home():
    return {"message": "Car Price Prediction API Running"}

@app.post("/predict")
def predict_price(data: CarFeatures):

    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    return {"predicted_price": float(prediction[0])}

    