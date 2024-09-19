import requests

# General function to call an API
def make_api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
