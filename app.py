import streamlit as st
from frankfurter import get_latest_rate, get_historical_rate
from currency import format_conversion

st.title('FX Converter')

# List of available currencies (you can add more as supported by the Frankfurter API)
available_currencies = ['AUD', 'USD', 'EUR', 'GBP', 'JPY', 'CAD', 'INR', 'CNY', 'NZD', 'CHF']

# Inputs
amount = st.number_input('Enter the amount to be converted:', value=01.0, step=1.0)
from_currency = st.selectbox('From Currency:', available_currencies)
to_currency = st.selectbox('To Currency:', available_currencies)


# Button to get the latest rate (current date)
if st.button('Get Latest Rate'):
    rate_info = get_latest_rate(from_currency, to_currency)
    if rate_info:
        formatted_result = format_conversion(amount, rate_info['rate'], rate_info['inverse_rate'], from_currency, to_currency, 'today')
        st.write(formatted_result)
    else:
        st.error('Failed to retrieve conversion rate. Please try again.')

selected_date = st.date_input('Select a date for historical rates:', value=None)
# Button to get conversion rate for a selected date
if st.button('Conversion Rate'):
    if selected_date:
        rate_info = get_historical_rate(from_currency, to_currency, selected_date)
        if rate_info:
            formatted_result = format_conversion(amount, rate_info['rate'], rate_info['inverse_rate'], from_currency, to_currency, selected_date)
            st.write(formatted_result)
        else:
            st.error('Failed to retrieve conversion rate. Please try again.')
    else:
        st.error('Please select a date to get the historical conversion rate.')
