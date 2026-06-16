import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_single_post_returns_200():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_single_post_has_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_get_single_post_correct_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1

def test_get_nonexistent_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404