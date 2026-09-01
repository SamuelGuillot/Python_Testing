def test_purchase_places_success(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': 2
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

    clubs, competitions, bookings = mock_data()
    club = next(c for c in clubs if c['name'] == 'Simply Lift')
    comp = next(c for c in competitions if c['name'] == 'Spring Gala')
    assert int(club['points']) == 11     # 13 - 2
    assert int(comp['numberOfPlaces']) == 23  # 25 - 2


def test_book_club_not_found(client):
    response = client.get('/book/Spring Gala/FakeClub')
    assert response.status_code == 404
    assert b'Club not found. Please try again.' in response.data

def test_book_competition_not_found(client):
    response = client.get('/book/Unknown/Simply Lift')
    assert response.status_code == 404
    assert b'Competition missing. Please try again.' in response.data

def test_purchase_places_invalid_club(client):
    response = client.post('/purchasePlaces', data={
        'club': 'Fake Club',
        'competition': 'Spring Gala',
        'places': '2'
    })
    assert response.status_code == 404
    assert b'Invalid data.' in response.data

def test_purchase_places_invalid_competition(client):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Unknown Comp',
        'places': '2'
    })
    assert response.status_code == 404
    assert b'Invalid data.' in response.data

def test_purchase_places_non_numeric(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': 'abc'
    })
    assert response.status_code == 200
    assert b'Enter a valid number.' in response.data

def test_purchase_places_negative(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '-1'
    })
    assert response.status_code == 200
    assert b'Please enter a positive number of places.' in response.data