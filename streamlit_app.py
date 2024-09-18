import streamlit as st
import requests
from datetime import datetime

# API URL
api_url = "https://api.frankfurter.app"

# Fetch available currencies
currencies_url = f"{api_url}/currencies"
currencies_response = requests.get(currencies_url)
currencies = currencies_response.json()

# App Title
st.title("FX Converter")

# Input for amount
amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=50.0)

# Select currencies (From and To)
from_currency = st.selectbox("From Currency:", currencies.keys(), index=0)
to_currency = st.selectbox("To Currency:", currencies.keys(), index=1)

# Button for getting the latest rate
if st.button("Get Latest Rate"):
    latest_url = f"{api_url}/latest?amount={amount}&from={from_currency}&to={to_currency}"
    latest_response = requests.get(latest_url).json()
    converted_amount = latest_response["rates"][to_currency]
    st.write(f"### {amount} {from_currency} = {converted_amount} {to_currency}")

# Select a date for historical rates
selected_date = st.date_input("Select a date for historical rates:", value=datetime.today())

# Button for fetching historical rate
if st.button("Conversion Rate"):
    historical_url = f"{api_url}/{selected_date}?amount={amount}&from={from_currency}&to={to_currency}"
    historical_response = requests.get(historical_url).json()
    historical_rate = historical_response["rates"][to_currency]
    st.write(f"### On {selected_date}, {amount} {from_currency} = {historical_rate} {to_currency}")
