import pytest
from finders import find_club_by_email, find_club_by_name, find_competition_by_name

def test_find_club_by_email_found():
    clubs = [{'name': 'Simply Lift', 'email': 'john@example.com'}]
    result = find_club_by_email('john@example.com', clubs)
    assert result == clubs[0]

def test_find_club_by_email_not_found():
    clubs = [{'name': 'Simply Lift', 'email': 'john@example.com'}]
    result = find_club_by_email('unknown@example.com', clubs)
    assert result is None

def test_find_club_by_name_found():
    clubs = [{'name': 'Simply Lift', 'email': 'john@example.com'}]
    result = find_club_by_name('Simply Lift', clubs)
    assert result == clubs[0]

def test_find_club_by_name_not_found():
    clubs = [{'name': 'Simply Lift', 'email': 'john@example.com'}]
    result = find_club_by_name('Fake Club', clubs)
    assert result is None

def test_find_competition_by_name_found():
    comps = [{'name': 'Spring Gala', 'date': '2026-10-22', 'numberOfPlaces': '25'}]
    result = find_competition_by_name('Spring Gala', comps)
    assert result == comps[0]

def test_find_competition_by_name_not_found():
    comps = [{'name': 'Spring Gala', 'date': '2026-10-22', 'numberOfPlaces': '25'}]
    result = find_competition_by_name('Unknown', comps)
    assert result is None