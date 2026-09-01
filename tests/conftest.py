import copy
import pytest
from app import create_app
import routes.main
import tempfile
import os
import database

import pytest
from freezegun import freeze_time

@pytest.fixture(autouse=True)
def freeze_time_for_tests():
    with freeze_time("2025-01-01"):
        yield

        
@pytest.fixture(autouse=True)
def temp_files(monkeypatch):
    temp_dir = tempfile.mkdtemp()
    monkeypatch.setattr(database, 'BOOKINGS_FILE', os.path.join(temp_dir, 'bookings.json'))
    monkeypatch.setattr(database, 'CLUBS_FILE', os.path.join(temp_dir, 'clubs.json'))
    monkeypatch.setattr(database, 'COMPETITIONS_FILE', os.path.join(temp_dir, 'competitions.json'))
    yield

TEST_CLUBS = [
    {'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': 13},
    {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': 4},
    {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': 12},
]

TEST_COMPETITIONS = [
    {'name': 'Spring Gala', 'date': '2026-10-22 10:00:00', 'numberOfPlaces': 25},
    {'name': 'Fall Classic', 'date': '2026-11-15 10:00:00', 'numberOfPlaces': 0},
    {'name': 'Kawazaki', 'date': '2028-10-22 13:30:00', 'numberOfPlaces': 15},
]

@pytest.fixture(scope='function')
def client(monkeypatch):
    app = create_app()
    app.config['SECRET_KEY'] = 'test_secret'
    app.config['TESTING'] = True

    routes.main.clubs = copy.deepcopy(TEST_CLUBS)
    routes.main.competitions = copy.deepcopy(TEST_COMPETITIONS)
    routes.main.bookings = {}

    monkeypatch.setattr(routes.main, 'save_bookings', lambda *args, **kwargs: True)
    monkeypatch.setattr(routes.main, 'save_competitions', lambda *args, **kwargs: True)
    monkeypatch.setattr(routes.main, 'save_clubs', lambda *args, **kwargs: True)

    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_data():
    def get_fresh_data():
        from routes.main import clubs, competitions, bookings
        return copy.deepcopy(clubs), copy.deepcopy(competitions), copy.deepcopy(bookings)
    return get_fresh_data