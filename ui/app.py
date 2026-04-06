import streamlit as st
import requests

st.title("CESAR: Real Estate Assistant")
st.write("Enter the details of the property to get an estimated price and safety level.")

API_URL = "http://localhost:8000"

surface = float(st.number_input("Surface (m²)", min_value=1.0, max_value=500.0, value=50.0))
rooms = int(st.number_input("Number of rooms", min_value=1, max_value=20, step=1, value=3))
department_options = {
    "75 - Paris": 75,
    "77 - Seine-et-Marne": 77,
    "78 - Yvelines": 78,
    "91 - Essonne": 91,
    "92 - Hauts-de-Seine": 92,
    "93 - Seine-Saint-Denis": 93,
    "94 - Val-de-Marne": 94,
    "95 - Val-d'Oise": 95,
}

department_label = st.selectbox("Department", list(department_options.keys()))
department =  int(department_options[department_label])


if st.button("Estimate"):
    response = requests.post(f"{API_URL}/predict", json={
        "surface": surface,
        "rooms": rooms,
        "department": department,
    })
    
    if response.status_code == 200:
        result = response.json()
        st.metric("Estimated Price", f"{result['estimated_price']:,.0f} €")
        st.metric("Safety Level", result["safety_level"])
    else:
        st.error("API error")