from flask import jsonify
import random

def get_random_countries(country_data, count=2):
    return random.sample(country_data, count)

def check_guess(current_country, new_country, user_guess):
    if (user_guess == 'h' and new_country['population'] > current_country['population']) or \
       (user_guess == 'l' and new_country['population'] < current_country['population']):
        return 'correct'
    else:
        return 'wrong'

def play_game_round(current_country, new_country, user_guess, country_data):
    if check_guess(current_country, new_country, user_guess) == 'correct':

        next_country = random.choice(country_data)
        while next_country['name']['common'] == new_country['name']:
            next_country = random.choice(country_data)

        answer = 'lower' if new_country['population'] > current_country['population'] else 'higher'

        return jsonify({
            'result': 'correct',
            'answer': answer,
            'new_country': {
                'name': next_country['name']['common'],
                'population': next_country['population'],
                'flags': next_country['flags']['svg']
            }
        })
    else:
        return jsonify({
            'result': 'wrong'
        })
