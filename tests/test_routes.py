def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'PhishGuard' in response.data

def test_analyze_valid_url(client):
    response = client.post('/analyze', data={'url': 'https://www.google.com'})
    assert response.status_code == 200
    assert b'SAFE' in response.data or b'SUSPICIOUS' in response.data or b'DANGER' in response.data

def test_analyze_empty_url(client):
    response = client.post('/analyze', data={'url': ''})
    assert response.status_code == 302
    assert response.headers['Location'] == '/'
