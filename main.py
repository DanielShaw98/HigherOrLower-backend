from api import fetch_all_countries
from game import get_random_countries, play_game_round

if __name__ == "__main__":
    country_data = fetch_all_countries()
    countries = get_random_countries(country_data, 1)
    current_country = countries[0]
    while current_country:
        current_country = play_game_round(country_data, current_country)
