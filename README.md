# CESAR – Real Estate Assistant API

## Intro
Remember the exitement of moving to a new city in France? But before that we've all been through a hard time looking for the "right" accomoadation. Have you ever found out that you are paying too much for the purchase price/rent when comparing it to your neighbors? Have you had an experience that thinking you've found a "good bargain" but realised that the community is not safe and that's why the price is so low. These two small problems are annoying and could ruins your start of life at a new city.
 
That's where CESAR comes in. We provides you the fair price and mind you the pitfalls that you might encounter when looking for an accomodation in a new city in France.

## What is CESAR?


CESAR is a Real Estate Assistant which gives an estimate of the price/rent based on the input of the features of the propety(Surfaces, Number of Rooms, Address). Moreover it would suggest you the safety level of the region. 

It is designed as a building block for a real estate platform where users need quick price estimations before making decisions. 

Typical users:

- new comers of the city who are looking for an accomodation but have completely no clues about it (foreign students, new foreign employees,new immigrants etc)

- individuals who are considering about changing their current accomodations but not familiar with the real estate market

- platforms providing decision support tools (suggest suitable listing prices for the property owner)

---

## Why is this useful?

Property valuation is a key step in real estate decisions.

In traditional real estate valuing process, it needs the buyers to do a lot of research on the previous transactions prices and current listing prices of similar properties to get an objective valuation of the price. This would takes a lot of effort, and for those who are not sure which area would they like to live in, it would be impossible to have a clear understanding of every potential areas they would like to live.  

Moreover, not like information like commune time, life convenience which could be easily achieved from Google Map. Safety levels are not easy to be found by people, especially for those who are not familiar with the government data system of France.

To solve these two problem, we build CESAR, which can:
- give users a data-based price reference 
- suggest the safety level of the community
- be integrated into larger workflows (search, audit, anomaly detection)

With the 2 main functions of CESAR, User could find the real "hidden-gem" which are of good price with no potential pitfalls.

---

## What does the system do?

The system exposes a simple model through a FastAPI service.

Data we used:
- Demande de Valeurs Foncières （dvf）of ile-de-france from https://explore.data.gouv.fr/


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



---

## Implementation of CESAR

### Prerequisites
- Python 3.12+

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


---

## Limitations

This is not a production-grade valuation system.

Current limitations:
- we only support the purchase of a real estate, rental is not supported
- the safety level of each department are predefined by human rather than data-based
- currently we only support the prediction for ile-de-france
- the price predict models are simple and not fine-tuned
- the address is only precise to department 
- no evaluation of model accuracy
- no anomaly detection
- no monitoring or logging
- no scaling strategy



---

## What would be needed for production?

To move toward a real product, we would need:

- extend the support area to whole France
- add predict functions for rental based on the rental data
- create a safety level model based on the data from https://www.data.gouv.fr/fr/datasets/bases-statistiques-communale-et-departementale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/
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

- keeping the data updated
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
