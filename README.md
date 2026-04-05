# CESAR – Property Price Estimation API

## What is this?

CESAR is a minimal service that estimates the price of a property based on a few basic inputs (surface and number of rooms).

It is designed as a building block for a real estate platform where users need quick price estimations before making decisions.

Typical users:
- individuals evaluating a potential purchase
- platforms providing decision support tools

---

## Why is this useful?

Property valuation is a key step in real estate decisions.

Even a simple estimation tool can:
- give users a first price reference
- support filtering and comparison
- be integrated into larger workflows (search, audit, anomaly detection)

This project demonstrates how such a tool can be delivered as a reliable API.

---

## What does the system do?

The system exposes a simple model through a FastAPI service.

Input:
- surface
- number of rooms

Output:
- estimated price

Endpoints:
- POST /predict → returns a price estimate
- GET /health → service status
- GET /model_info → model metadata

---

## Approach

We intentionally keep the model simple and focus on:

- turning a model into a usable service
- defining a clear API contract
- ensuring the system can be extended

The system is designed so that the model can be replaced without changing the API.

---

## Limitations

This is not a production-grade valuation system.

Current limitations:
- no real data or training process
- no evaluation of model accuracy
- no anomaly detection
- no monitoring or logging
- no scaling strategy

---

## What would be needed for production?

To move toward a real product, we would need:

- a trained model based on real datasets
- performance evaluation and validation
- monitoring (latency, errors)
- deployment infrastructure (containers, cloud)
- failure handling and retry mechanisms
- cost management

---

## Team reliability and risks

The current implementation shows that we can:

- build a functional ML service
- expose it via API
- structure a simple system

However, we would need support for:

- data engineering
- model validation
- production deployment

---

## Maintainer considerations

If this system were in production, updating the model would require:

- keeping API compatibility (do not break input/output format)
- versioning the model
- testing before deployment
- monitoring after release

A safe release process would include:
- validation on test data
- rollback strategy in case of failure

---

## Conclusion

This project demonstrates a minimal but complete ML system:

Model → API → Usable service

The focus is not on model performance, but on delivering a usable and extensible component in a larger system.
