from api import fetch_data

def get_latest_rate(from_currency, to_currency):
    endpoint = f"latest?from={from_currency}&to={to_currency}"
    data = fetch_data(endpoint)
    if data and 'rates' in data:
        rate = data['rates'][to_currency]
        inverse_rate = 1 / rate
        return {'rate': rate, 'inverse_rate': inverse_rate}
    return None

def get_historical_rate(from_currency, to_currency, date):
    endpoint = f"{date}?from={from_currency}&to={to_currency}"
    data = fetch_data(endpoint)
    if data and 'rates' in data:
        rate = data['rates'][to_currency]
        inverse_rate = 1 / rate
        return {'rate': rate, 'inverse_rate': inverse_rate}
    return None
