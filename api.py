import requests

API_URL = "https://api.frankfurter.app"


def make_api_call(endpoint):
    """Make a call to the Frankfurter API."""
    url = f"{API_URL}{endpoint}"
    response = requests.get(url)

    if response.status_code == 404:
        raise Exception(f"API request failed with status code 404: The endpoint {url} was not found.")

    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")

    return response.json()
