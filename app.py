import streamlit as st
from frankfurter import get_latest_rate, get_historical_rate, get_available_currencies
from currency import format_conversion_result
from datetime import date

# Title
st.title("FX Converter")

# Fetch available currencies from Frankfurter API
currencies = get_available_currencies()

# Input fields
amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=50.0, step=0.01)
from_currency = st.selectbox("From Currency:", currencies)
to_currency = st.selectbox("To Currency:", currencies)

# Get today's date for the latest rate
today = date.today()

# Get Latest Rate Button
if st.button("Get Latest Rate"):
    if from_currency == to_currency:
        st.error("Please select different currencies for conversion.")
    else:
        rate, inverse_rate, conversion_text = get_latest_rate(from_currency, to_currency, amount)
        st.write(format_conversion_result(rate, inverse_rate, conversion_text))


# Date input for historical rates
conversion_date = st.date_input("Select a date for historical rates:", today)


# Get Historical Conversion Rate Button
if st.button("Conversion Rate"):
    if from_currency == to_currency:
        st.error("Please select different currencies for conversion.")
    else:
        rate, inverse_rate, conversion_text = get_historical_rate(from_currency, to_currency, amount, conversion_date)
        st.write(format_conversion_result(rate, inverse_rate, conversion_text))
