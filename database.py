import json
import logging
import os

BOOKINGS_FILE = os.environ.get('BOOKINGS_FILE', 'bookings.json')
CLUBS_FILE = os.environ.get('CLUBS_FILE', 'clubs.json')
COMPETITIONS_FILE = os.environ.get('COMPETITIONS_FILE', 'competitions.json')

logging.basicConfig(level=logging.ERROR)

def load_json(file_path, key=None):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data.get(key, []) if key else data
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
        logging.error(f"Erreur lecture {file_path}: {e}")
        return [] if key else {}

def save_json(file_path, data, key=None):
    try:
        payload = {key: data} if key else data
        with open(file_path, 'w') as f:
            json.dump(payload, f, indent=4)
        return True
    except PermissionError as e:
        logging.error(f"Erreur écriture {file_path}: {e}")
        return False

def load_clubs():
    return load_json(CLUBS_FILE, key='clubs')

def save_clubs(clubs_list):
    return save_json(CLUBS_FILE, clubs_list, key='clubs')

def load_competitions():
    return load_json(COMPETITIONS_FILE, key='competitions')

def save_competitions(competitions_list):
    return save_json(COMPETITIONS_FILE, competitions_list, key='competitions')

def load_bookings():
    return load_json(BOOKINGS_FILE)   # flat dict

def save_bookings(bookings_dict):
    return save_json(BOOKINGS_FILE, bookings_dict)