from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

model = joblib.load("artifacts/model_pipeline.pkl")
app = FastAPI()

class CarFeatures(BaseModel):

    brand: str = Field(..., description="Brand of the car")
    model: str = Field(..., description="Model of the car")
    vehicle_age: int = Field(..., ge=0, le=30, description="Vehicle age in years")
    km_driven: int = Field(..., ge=0, le=1000000, description="Kilometers driven")
    seller_type: str = Field(..., description="Seller type")
    fuel_type: str = Field(..., description="Fuel type")
    transmission_type: str = Field(..., description="Transmission type")
    mileage: float = Field(..., ge=0, description="Mileage in km/l")
    engine: int = Field(..., ge=500, le=5000, description="Engine displacement in cc")
    max_power: float = Field(..., ge=0, description="Maximum power in bhp")
    seats: int = Field(..., ge=2, le=10, description="Number of seats")

@app.get("/")
def home():
    return {"message": "Car Price Prediction API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_price(data: CarFeatures):
    try:
        input_data = pd.DataFrame([data.dict()])
        prediction = model.predict(input_data)
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
   