from datetime import datetime, timedelta

def test_purchase_places_past_competition(client, monkeypatch, mock_data):
    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    past_comp = [{'name': 'Past Event', 'date': past_date, 'numberOfPlaces': '20'}]
    monkeypatch.setattr('routes.main.competitions', past_comp)

    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Past Event',
        'places': 2
    })
    assert b'Cannot purchase places for a past competition.' in response.data

def test_purchase_places_not_enough_points(client, mock_data):
    response = client.post('/purchasePlaces', data={
        'club': 'Iron Temple',
        'competition': 'Spring Gala',
        'places': '5'
    })
    assert response.status_code == 200
    assert b'Your club does not have enough points (you have 4).' in response.data

def test_purchase_places_more_than_12_total(client, mock_data):
    # Réserver 10 places
    client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': '10'
    })
    # Tenter 3 places de plus
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