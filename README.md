# CESAR – Minimal MLOps Property Valuation System

## Overview

This project implements a minimal end-to-end MLOps pipeline.

It takes simple input data, applies a model, and exposes predictions through an API.

Pipeline:

Input → Model → API → Prediction

---

## Goal

Estimate property price using basic features:

- surface (square meters)
- number of rooms

The focus is on system design, not model accuracy.

---

## Features

- Simple prediction model
- FastAPI service
- REST API endpoints
- Health check endpoint

---

## API Endpoints

POST /predict  
→ Returns estimated price

GET /health  
→ Returns service status

---

## Project Structure

cesar/
  app/
    main.py
  model/
    predict.py
  data/
  README.md
  requirements.txt

---

## How to Run

Install dependencies:

python3 -m pip install -r requirements.txt

Start the API:

python3 -m uvicorn app.main:app --reload

Open in browser:

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

## MLOps Concepts

This project demonstrates:

- Simple deployable ML system
- API-based model serving
- Clear input/output contract
- Reproducible setup

---

## Notes

This is a minimal educational implementation.
