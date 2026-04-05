# CESAR – Minimal MLOps Property Valuation System

## TL;DR

This project demonstrates a minimal end-to-end MLOps pipeline:

Input → Model → API → Prediction

A simple model is exposed through a FastAPI service and can be queried via HTTP.

---

## Goal

Estimate the value of a property using basic features:

- surface (in square meters)
- number of rooms

This project focuses on system design rather than model performance.

---

## System Overview

The system includes:

- A simple prediction model (predict_price)
- A FastAPI application exposing the model
- A REST API interface for inference

Endpoints:

- POST /predict → return estimated price
- GET /health → check if the service is running

---

## Project Structure

cesar/
  app/
    main.py        # FastAPI application
  model/
    predict.py     # Model logic
  data/            # Optional data folder
  README.md
  requirements.txt

---

## How to Run

1. Install dependencies

python3 -m pip install -r requirements.txt

2. Start the API

python3 -m uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

3. Test the API

Open:

http://127.0.0.1:8000/docs

---

## Example

Request:

{
  "surface": 50,
  "rooms": 3
}

Response:

{
  "estimated_price": 180000
}

---
# CESAR – Minimal MLOps Property Valuation System

## TL;DR

This project demonstrates a minimal end-to-end MLOps pipeline:

Input → Model → API → Prediction

A simple model is exposed through a FastAPI service and can be queried via HTTP.

---

## Goal

Estimate the value of a property using basic features:

- surface (in square meters)
- number of rooms

This project focuses on system design rather than model performance.

---

## System Overview

The system includes:

- A simple prediction model (predict_price)
- A FastAPI application exposing the model
- A REST API interface for inference

Endpoints:

- POST /predict → return estimated price
- GET /health → check if the service is running

---

## Project Structure

cesar/
  app/
    main.py        # FastAPI application
  model/
    predict.py     # Model logic
  data/            # Optional data folder
  README.md
  requirements.txt

---

## How to Run

1. Install dependencies

python3 -m pip install -r requirements.txt

2. Start the API

python3 -m uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000

3. Test the API

Open:

http://127.0.0.1:8000/docs

---

## Example

Request:

{
  "surface": 50,
  "rooms": 3
}

Response:

{
  "estimated_price": 180000
}

---

## Key MLOps Concepts Demonstrated

- Simplicity first (minimal working system)
- Model deployment via API
- Reproducibility
- Clear API contract

---

## Notes

This is a minimal implementation for educational purposes.

The goal is to demonstrate how a machine learning model can be turned into a usable system.
