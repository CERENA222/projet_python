import requests

base_url = "http://127.0.0.1:8000"


def test_get_artists():
    # Test retrieving artists with a specific name (e.g., U2)
    response = requests.get(f"{base_url}/artists/U2")
    # Assert that the HTTP response status code is 200 (OK)
    assert response.status_code == 200
    # Parse the JSON response data
    data = response.json()
    # Assert that there is at least one artist returned
    assert len(data) > 0


def test_get_albums():
    # Test retrieving albums for an artist with ID 1
    response = requests.get(f"{base_url}/albums/1")
    # Assert that the HTTP response status code is 200 (OK)
    assert response.status_code == 200
    # Parse the JSON response data
    data = response.json()
    # Assert that there is at least one album returned
    assert len(data) > 0


def test_get_tracks():
    # Test retrieving tracks for an album with ID 1
    response = requests.get(f"{base_url}/tracks/1")
    # Assert that the HTTP response status code is 200 (OK)
    assert response.status_code == 200
    # Parse the JSON response data
    data = response.json()
    # Assert that there is at least one track returned
    assert len(data) > 0
