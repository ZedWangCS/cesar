from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict_price
from model.safety import get_safety_level

app = FastAPI()

class InputData(BaseModel):
    surface: float
    rooms: int
    department: int

@app.get("/")
def read_root():
    return {"message": "CESAR API is running"}

@app.post("/predict")
def predict(data: InputData):
    price = predict_price(data.surface, data.rooms, data.department)
    safety = get_safety_level(data.department)
    return {
        "estimated_price": price,
        "safety_level": safety
        }
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/model_info")
def model_info():
    return {
        "model_name": "random_forest_model",
        "version": "1.0",
        "inputs": ["surface", "rooms", "department"]
    }
