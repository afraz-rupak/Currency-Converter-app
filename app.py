import streamlit as st
from datetime import datetime
from frankfurter import get_latest_rate, get_historical_rate, get_available_currencies
from currency import format_conversion_result

# Fetch available currencies dynamically
available_currencies = get_available_currencies()

# App Title
st.title("FX Converter")

# Input for amount options
amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=50.0)

# Select currencies (From and To)
from_currency = st.selectbox("From Currency:", available_currencies.keys())
to_currency = st.selectbox("To Currency:", available_currencies.keys())

# Latest Rate Button
if st.button("Get Latest Rate"):
    latest_rate = get_latest_rate(from_currency, to_currency, amount)
    formatted_result = format_conversion_result(amount, from_currency, to_currency, latest_rate, "latest")
    st.write(formatted_result)

# Historical Rate Section
selected_date = st.date_input("Select a date for historical rates:", value=datetime.today())

# Historical Rate Button
if st.button("Conversion Rate"):
    historical_rate = get_historical_rate(from_currency, to_currency, amount, selected_date)
    formatted_result = format_conversion_result(amount, from_currency, to_currency, historical_rate, selected_date)
    st.write(formatted_result)
