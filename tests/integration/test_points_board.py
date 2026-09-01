def test_points_board_shows_all_clubs(client, mock_data):
    response = client.get('/points')
    assert response.status_code == 200
    assert b'Club Points Board' in response.data
    assert b'Simply Lift' in response.data
    assert b'13' in response.data
    assert b'Iron Temple' in response.data
    assert b'4' in response.data
    assert b'She Lifts' in response.data
    assert b'12' in response.data

def test_points_board_sorted_descending(client, mock_data):
    response = client.get('/points')
    html = response.data.decode()
    pos_she = html.find('She Lifts')
    pos_iron = html.find('Iron Temple')
    assert pos_she > 0 and pos_iron > 0 and pos_she < pos_iron

def test_points_board_links_back_home(client):
    response = client.get('/points')
    assert b'Home' in response.data
    assert b'href="/"' in response.data or b'href="' in response.data