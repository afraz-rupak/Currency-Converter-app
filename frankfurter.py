from api import make_api_call

# Fetch available currency codes
def get_available_currencies():
    url = "https://www.frankfurter.app/currencies"
    data = make_api_call(url)
    if data:
        return list(data.keys())
    return []

# Fetch the latest conversion rate
def get_latest_rate(from_currency, to_currency, amount):
    url = f"https://www.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    data = make_api_call(url)
    if data:
        rate = data['rates'][to_currency]
        inverse_rate = 1 / rate
        conversion_text = f"The conversion rate on {data['date']} from {from_currency} to {to_currency} was {rate}. " \
                          f"So {amount} in {from_currency} corresponds to {amount * rate:.2f} in {to_currency}."
        return rate, inverse_rate, conversion_text
    return None, None, "Failed to retrieve data."

# Fetch the historical conversion rate
def get_historical_rate(from_currency, to_currency, amount, conversion_date):
    formatted_date = conversion_date.strftime("%Y-%m-%d")
    url = f"https://www.frankfurter.app/{formatted_date}?from={from_currency}&to={to_currency}"
    data = make_api_call(url)
    if data:
        rate = data['rates'][to_currency]
        inverse_rate = 1 / rate
        conversion_text = f"The conversion rate on {formatted_date} from {from_currency} to {to_currency} was {rate}. " \
                          f"So {amount} in {from_currency} corresponds to {amount * rate:.2f} in {to_currency}."
        return rate, inverse_rate, conversion_text
    return None, None, "Failed to retrieve data."
