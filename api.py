import requests

BASE_URL = 'https://restcountries.com/v3.1/all'

def fetch_all_countries():
    fields = "name,flags,population"
    response = requests.get(f"{BASE_URL}?fields={fields}")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
