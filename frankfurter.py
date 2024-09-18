from api import make_api_call

def get_available_currencies():
    """Fetch all available currencies from Frankfurter API."""
    endpoint = "/currencies"
    return make_api_call(endpoint)

def get_latest_rate(from_currency, to_currency, amount):
    """Get the latest conversion rate for a currency pair."""
    if from_currency == to_currency:
        return 1.0  # Return a conversion rate of 1 if currencies are the same
    endpoint = f"/latest?amount={amount}&from={from_currency}&to={to_currency}"
    data = make_api_call(endpoint)
    return data["rates"][to_currency]

def get_historical_rate(from_currency, to_currency, amount, date):
    """Get historical conversion rate for a specific date."""
    if from_currency == to_currency:
        return 1.0  # Return a conversion rate of 1 if currencies are the same
    formatted_date = date.strftime("%Y-%m-%d")
    endpoint = f"/{formatted_date}?amount={amount}&from={from_currency}&to={to_currency}"
    data = make_api_call(endpoint)
    return data["rates"][to_currency]
