import pytest
from datetime import datetime
from validators import validate_and_prepare_booking

def test_validate_booking_success():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'date': '2028-10-22 13:30:00', 'numberOfPlaces': 15}
    bookings = {}
    current = datetime(2026, 8, 6)
    valid, msg, max_allowed = validate_and_prepare_booking(club, comp, 5, bookings, current)
    assert valid is True
    assert msg is None
    assert max_allowed == 12

def test_validate_booking_past_competition():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Past Event', 'date': '2020-01-01 10:00:00', 'numberOfPlaces': 25}
    bookings = {}
    current = datetime(2026, 8, 6)
    valid, msg, max_allowed = validate_and_prepare_booking(club, comp, 5, bookings, current)
    assert valid is False
    assert 'past' in msg.lower()
    assert max_allowed == 0

def test_validate_booking_negative_places():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'date': '2028-10-22 13:30:00', 'numberOfPlaces': 15}
    bookings = {}
    current = datetime(2026, 8, 6)
    valid, msg, max_allowed = validate_and_prepare_booking(club, comp, -1, bookings, current)
    assert valid is False
    assert 'positive' in msg.lower()
    assert max_allowed == 0

def test_validate_booking_exceeds_max():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'date': '2028-10-22 13:30:00', 'numberOfPlaces': 15}
    bookings = {'Simply Lift': {'Kawazaki': 5}}
    current = datetime(2026, 8, 6)
    valid, msg, max_allowed = validate_and_prepare_booking(club, comp, 10, bookings, current)
    assert valid is False
    assert 'You can only book 7 more place(s) due to the 12 place limit.' in msg
    assert max_allowed == 7