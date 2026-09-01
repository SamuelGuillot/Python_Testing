def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'GUDLFT Registration' in response.data

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302   # redirect to index

def test_show_summary_valid_email(client, mock_data):
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    assert response.status_code == 200
    assert b'Welcome, john@simplylift.co' in response.data

def test_show_summary_invalid_email(client):
    response = client.post('/showSummary', data={'email': 'unknown@test.com'})
    assert response.status_code == 200
    assert b'Email not found. Please try again.' in response.data