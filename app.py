from flask import Flask, request, jsonify
from flask_cors import CORS
from api import fetch_all_countries
from game import get_random_countries, play_game_round
import os

app = Flask(__name__)
CORS(app)

country_data = fetch_all_countries()

@app.route('/start-game', methods=['POST'])
def start_game():
    countries = get_random_countries(country_data, 2)
    current_country = countries[0]
    new_country = countries[1]

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
    data = request.json
    current_country = data['current_country']
    new_country = data['new_country']
    user_guess = data['guess']

    result = play_game_round(current_country, new_country, user_guess, country_data)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)), debug=True)
