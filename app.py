from flask import Flask, request, jsonify
from flask_cors import CORS
from api import fetch_all_countries
from game import get_random_countries, play_game_round
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
CORS(app)

country_data = fetch_all_countries()
used_countries = []

@app.route('/start-game', methods=['POST'])
def start_game():
    global used_countries
    used_countries.clear()
    countries = get_random_countries(country_data, 2)
    current_country = countries[0]
    new_country = countries[1]
    used_countries.extend([current_country['name']['common'], new_country['name']['common']])

    return jsonify({
        'current_country': {
            'name': current_country['name']['common'],
            'population': current_country['population'],
            'flags': current_country['flags']['svg']
        },
        'new_country': {
            'name': new_country['name']['common'],
            'population': new_country['population'],
            'flags': new_country['flags']['svg']
        }
    })

@app.route('/submit-guess', methods=['POST'])
def submit_guess():
    global used_countries
    data = request.json
    current_country = data['current_country']
    new_country = data['new_country']
    user_guess = data['guess']

    result = play_game_round(current_country, new_country, user_guess, country_data, used_countries)
    return result

if __name__ == '__main__':
    app.run(port=8000, debug=True)
