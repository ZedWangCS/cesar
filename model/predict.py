import joblib
from pathlib import Path

#load the model
model_path = Path(__file__).parent / "model.joblib"
model = joblib.load(model_path)

def predict_price(surface: float, rooms: int) -> float:
    prediction = model.predict([[surface, rooms]])
    return float(prediction[0])

