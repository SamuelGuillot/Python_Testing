from operations import apply_booking

def test_apply_booking_updates_correctly():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {}

    apply_booking(club, comp, 3, bookings)

    assert club['points'] == 10
    assert comp['numberOfPlaces'] == 12
    assert bookings['Simply Lift']['Kawazaki'] == 3

def test_apply_booking_creates_new_entry_if_missing():
    club = {'name': 'Iron Temple', 'points': 10}
    comp = {'name': 'Fall Classic', 'numberOfPlaces': 20}
    bookings = {}

    apply_booking(club, comp, 4, bookings)

    assert bookings['Iron Temple']['Fall Classic'] == 4
    assert club['points'] == 6
    assert comp['numberOfPlaces'] == 16