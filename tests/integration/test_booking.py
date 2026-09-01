from datetime import datetime, timedelta

def test_book_future_competition(client, mock_data):
    response = client.get('/book/Spring Gala/Simply Lift')
    assert response.status_code == 200
    assert b'Spring Gala' in response.data
    assert b'Places available: 25' in response.data


def test_book_competition_not_found(client, mock_data):
    response = client.get('/book/Unknown/Simply Lift')
    assert response.status_code == 404
    assert b'Competition missing. Please try again.' in response.data


def test_book_club_not_found(client, mock_data):
    response = client.get('/book/Spring Gala/FakeClub')
    assert response.status_code == 404
    assert b'Club not found. Please try again.' in response.data


def test_book_past_competition(client, monkeypatch, mock_data):
    past_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
    past_comp = [{'name': 'Past Event', 'date': past_date, 'numberOfPlaces': '25'}]
    monkeypatch.setattr('routes.main.competitions', past_comp)

    response = client.get('/book/Past%20Event/Simply%20Lift')
    assert response.status_code == 200
    assert b'This competition has already taken place.' in response.data


def test_purchase_places_success(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '2'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

    clubs, competitions, bookings = mock_data()
    club = next(c for c in clubs if c['name'] == 'Simply Lift')
    comp = next(c for c in competitions if c['name'] == 'Spring Gala')
    assert int(club['points']) == 11
    assert int(comp['numberOfPlaces']) == 23


def test_purchase_places_not_enough_points(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Spring Gala',
        'places': '5'
    })
    assert response.status_code == 200
    assert b'Your club does not have enough points (you have 4).' in response.data


def test_purchase_places_more_than_12_total(client, mock_data):
    client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '10'
    })
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '3'
    })
    assert b'You can only book 2 more place(s) due to the 12 place limit.' in response.data


def test_purchase_places_competition_full(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Fall Classic',
        'places': '1'
    })
    assert b'Not enough places available in the competition (only 0 left).' in response.data


def test_purchase_places_past_competition(client, monkeypatch, mock_data):
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    past_comp = [{'name': 'Past Event', 'date': past_date, 'numberOfPlaces': '20'}]
    monkeypatch.setattr('routes.main.competitions', past_comp)

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Past Event',
        'places': '2'
    })
    assert b'Cannot purchase places for a past competition.' in response.data


def test_purchase_places_non_numeric(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': 'abc'
    })
    assert b'Enter a valid number.' in response.data


def test_purchase_places_negative(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '-1'
    })
    assert b'Please enter a positive number of places.' in response.data


def test_purchase_places_invalid_club(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Fake Club',
        'competition': 'Spring Gala',
        'places': '2'
    })
    assert response.status_code == 404
    assert b'Invalid data.' in response.data


def test_purchase_places_invalid_competition(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Unknown Comp',
        'places': '2'
    })
    assert response.status_code == 404
    assert b'Invalid data.' in response.data