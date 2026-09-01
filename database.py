import json

BOOKINGS_FILE = 'bookings.json'
CLUBS_FILE = 'clubs.json'
COMPETITIONS_FILE = 'competitions.json'

def load_clubs():
    with open(CLUBS_FILE) as c:
        return json.load(c)['clubs']

def save_clubs(clubs_list):
    with open(CLUBS_FILE, 'w') as c:
        json.dump({'clubs': clubs_list}, c, indent=4)

def load_competitions():
    with open(COMPETITIONS_FILE) as comps:
        return json.load(comps)['competitions']

def save_competitions(competitions_list):
    with open(COMPETITIONS_FILE, 'w') as comps:
        json.dump({'competitions': competitions_list}, comps, indent=4)

def load_bookings():
    try:
        with open(BOOKINGS_FILE) as b:
            return json.load(b)
    except FileNotFoundError:
        return {}

def save_bookings(bookings_dict):
    with open(BOOKINGS_FILE, 'w') as b:
        json.dump(bookings_dict, b, indent=4)