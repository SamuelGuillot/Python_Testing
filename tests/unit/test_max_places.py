from validators import compute_max_places

def test_compute_max_places_no_prior_bookings():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {}
    assert compute_max_places(club, comp, bookings) == 12

def test_compute_max_places_with_existing_bookings():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {'Simply Lift': {'Kawazaki': 5}} 
    assert compute_max_places(club, comp, bookings) == 12 - 5

def test_compute_max_places_points_limited():
    club = {'name': 'Iron Temple', 'points': 4}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {}
    assert compute_max_places(club, comp, bookings) == 4

def test_compute_max_places_places_limited():
    club = {'name': 'Simply Lift', 'points': 20}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 5}
    bookings = {}
    assert compute_max_places(club, comp, bookings) == 5

def test_compute_max_places_already_booked_12():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {'Simply Lift': {'Kawazaki': 12}}
    assert compute_max_places(club, comp, bookings) == 0