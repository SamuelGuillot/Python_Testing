from datetime import datetime
from validators import is_competition_past, validate_and_prepare_booking

def test_is_competition_past():
    past_comp = {'date': '2020-01-01 10:00:00'}
    future_comp = {'date': '2030-01-01 10:00:00'}
    current = datetime(2025, 1, 1)
    assert is_competition_past(past_comp, current) is True
    assert is_competition_past(future_comp, current) is False

def test_validate_booking_negative_places():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'date': '2028-10-22 13:30:00', 'numberOfPlaces': 15}
    bookings = {}
    current = datetime(2026, 8, 6)
    valid, msg, max_allowed = validate_and_prepare_booking(club, comp, -1, bookings, current)
    assert valid is False
    assert 'positive' in msg.lower()
    assert max_allowed == 0