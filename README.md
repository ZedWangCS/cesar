# CESAR – Accomodation Assistant API

## Intro
Remember the exitement of moving to a new city? But before that we've all been through a hard time looking for the "right" accomoadation. Scrolling through endless listings on different websites, looking for an accomodation with affordable and reasonable prices, wondering if the community is acually safe as advertised. All these small problems with accomodation are difficult to figure out for a new comer but any of these could entirely ruins the start of a new life.

That's where CESAR comes in. We provides you the fair price and mind you the pitfalls that you might encounter when looking for an accomodation in a new city.

## What is CESAR?


CESAR is an Accomodation Assistant which gives an estimate of the price based on the input of the features of the propety(Surfaces, Number of Rooms, Address). Moreover it would suggest you the things that you might ignore.

It is designed as a building block for a real estate platform where users need quick price estimations before making decisions. 

Typical users:

- new comers to the city who are looking for an accomodation but have no clues about it (foreign students, new employees,new immigrants etc)

- individuals who are considering about changing their current accomodations but not familiar with the property market

- platforms providing decision support tools (suggest suitable listing prices for the property owner)

---

## Why is this useful?

Property valuation is a key step in real estate decisions.

In traditional real estate process, it is hard to estimate the value. Usually we use the transaction price of a similar real estate as reference.However, usually the features would not be exactly the same to the very property we want to value.As a result, the valutaion would not be accurate as we want. Moreover, you could not find out the safety information of the community in the listing or Google Map. 

To solve these problem, we build CESAR, which can:
- give users a data-based price reference
- support filtering and comparison
- suggest the details that users might ignore
- be integrated into larger workflows (search, audit, anomaly detection)

This project demonstrates how such a tool can be delivered as a reliable API.

---

## What does the system do?

The system exposes a simple model through a FastAPI service.

Data we used:
- Demande de Valeurs Foncières（dvf） from https://explore.data.gouv.fr/


Input:
- surface
- number of rooms
- department

Output:
- estimated price
- safety level

Endpoints:
- POST /predict → returns a price estimate and safety level
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

## Implementation of CESAR

### Prerequisites
- Python 3.12+
- DVF data for Île-de-France departments (75, 77, 78, 91, 92, 93, 94, 95) placed in `data/`
- Available at: https://explore.data.gouv.fr/fr/immobilier

### Install dependencies
```bash
pip install -r requirements.txt
```

### Train the model
```bash
python -m model.train
```

### Start the API
```bash
uvicorn app.main:app --reload --port 8000
```

### Start the UI
Open a new terminal:
```bash
streamlit run ui/app.py
```

The UI will be available at http://localhost:8501

---

## Limitations

This is not a production-grade valuation system.

Current limitations:
- we only support the purchase of a real estate, rental is not supported
- currently we only support the prediction for ile-de-france
- the price predict models are simple and not fine-tuned
- no evaluation of model accuracy
- no anomaly detection
- no monitoring or logging
- no scaling strategy
- the address is only precise to department 
- the safety level prediction are not data-based

---

## What would be needed for production?

To move toward a real product, we would need:

- extend the support area to whole France
- add predict functions for rental 
- add other suggestions apart from the safety level
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
