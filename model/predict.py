import joblib
from pathlib import Path

#load the model
model_path = Path(__file__).parent / "model.joblib"
model = joblib.load(model_path)

def predict_price(surface: float, rooms: int, department: int) -> float:
    prediction = model.predict([[surface, rooms, department]])
    return float(prediction[0])

