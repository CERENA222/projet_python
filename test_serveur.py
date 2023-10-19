import requests

base_url = "http://127.0.0.1:8000"

def test_get_artists():
    response = requests.get(f"{base_url}/artists/U2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_albums():
    # l'artiste avec l'ID 1 a des albums
    response = requests.get(f"{base_url}/albums/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_tracks():
    # l'album avec l'ID 1 a des pistes
    response = requests.get(f"{base_url}/tracks/1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
