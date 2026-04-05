from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict_price

app = FastAPI()

class InputData(BaseModel):
    surface: float
    rooms: int

@app.get("/")
def read_root():
    return {"message": "CESAR API is running"}

@app.post("/predict")
def predict(data: InputData):
    price = predict_price(data.surface, data.rooms)
    return {
        "estimated_price": price
    }
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/model_info")
def model_info():
    return {
        "model_name": "simple_price_model",
        "version": "1.0",
        "inputs": ["surface", "rooms"]
    }
