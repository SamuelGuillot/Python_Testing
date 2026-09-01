from operations import apply_booking

def test_apply_booking_updates_correctly():
    club = {'name': 'Simply Lift', 'points': 13}
    comp = {'name': 'Kawazaki', 'numberOfPlaces': 15}
    bookings = {}

    apply_booking(club, comp, 3, bookings)

    assert club['points'] == 10  
    assert comp['numberOfPlaces'] == 12
    assert bookings['Simply Lift']['Kawazaki'] == 3