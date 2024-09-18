import streamlit as st
import requests
from datetime import datetime

api_url = "https://api.frankfurter.app"

currencies_url = f"{api_url}/currencies"
currencies_response = requests.get(currencies_url)
currencies = currencies_response.json()

st.title("FX Converter")

amount = st.number_input("Enter the amount to be converted:", min_value=0.0, value=50.0)

from_currency = st.selectbox("From Currency:", currencies.keys(), index=0)
to_currency = st.selectbox("To Currency:", currencies.keys(), index=1)

selected_date = st.date_input("Select a date for historical rates:", value=datetime.today())

if st.button("Conversion Rate"):
    historical_url = f"{api_url}/{selected_date}?amount={amount}&from={from_currency}&to={to_currency}"
    historical_response = requests.get(historical_url).json()
    historical_rate = historical_response["rates"][to_currency]
    historical_inverse_rate = 1 / historical_rate

    st.write(f"### Latest Conversion Rate")
    st.write(
        f"The conversion rate on {selected_date} from {from_currency} to {to_currency} was {historical_rate:.5f}. "
        f"So {amount} in {from_currency} correspond to {historical_rate * amount:.2f} in {to_currency}. "
        f"The inverse rate was {historical_inverse_rate:.4f}."
    )
