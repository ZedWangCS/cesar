# CESAR – Minimal MLOps Property Valuation System

## Overview

This project implements a minimal end-to-end MLOps pipeline.

It demonstrates how a machine learning model can be transformed into a usable service via an API.

Pipeline:

Input → Model → API → Prediction

---

## Business Context

We consider a startup building tools for people who want to buy real estate.

This system focuses on one core feature:
→ property value estimation

In a real product, this would be part of a larger system including:
- property search
- anomaly detection (unusual prices)
- decision support tools

---

## Goal

Estimate property price using simple features:

- surface (square meters)
- number of rooms

The goal is not model accuracy, but system design and usability.

---

## Features

- Simple prediction model
- FastAPI service
- REST API endpoints
- Health check endpoint
- Model information endpoint

---

## API Endpoints

POST /predict  
→ Returns estimated price

GET /health  
→ Returns service status

GET /model_info  
→ Returns model metadata

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

## MLOps Perspective

This project focuses on key MLOps principles:

- Simplicity first (minimal working system)
- Model deployment via API
- Clear input/output contract
- Reproducibility
- System thinking (model as a service)

---

## System Considerations

In real-world systems, additional aspects should be considered:

- Latency and throughput
- Scalability
- Failure handling (server or network issues)
- Monitoring and logging
- Cost efficiency

---

## Future Improvements

This system can be extended with:

- anomaly detection for unusual prices
- search functionalities
- UI integration
- containerization (Docker/Kubernetes)
- automated deployment (CI/CD)

---

## Notes

This is a minimal educational implementation.

The goal is to demonstrate how a machine learning model can be integrated into a usable and extensible system.
