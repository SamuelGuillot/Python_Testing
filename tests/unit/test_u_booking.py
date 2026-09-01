from datetime import datetime, timedelta

def test_book_past_competition(client, monkeypatch, mock_data):
    past_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
    past_comp = [{'name': 'Past Event', 'date': past_date, 'numberOfPlaces': '25'}]
    monkeypatch.setattr('routes.main.competitions', past_comp)

    response = client.get('/book/Past%20Event/Simply%20Lift')
    assert response.status_code == 200
    assert b'This competition has already taken place.' in response.data

def test_purchase_places_more_than_12_total(client, mock_data):
    # Réserver 10 places
    client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': 10
    })
    # 3 places de plus
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Gala',
        'places': 3
    })
    assert b'You can only book 2 more place(s) due to the 12 place limit.' in response.data