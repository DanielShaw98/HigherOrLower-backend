import requests

BASE_URL = 'https://restcountries.com/v3.1/all'

def fetch_all_countries():
    fields = "name,flags,population"
    response = requests.get(f"{BASE_URL}?fields={fields}")

    if response.status_code == 200:
        countries = response.json()
        filtered_countries = [country for country in countries if country['population'] > 0]
        return filtered_countries
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
