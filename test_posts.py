import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_session():
    session = requests.Session()
    yield session
    session.close()

def test_get_single_post_returns_200(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_single_post_has_expected_fields(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_get_single_post_correct_id(api_session):
    response = api_session.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1

def test_get_nonexistent_post_returns_404(api_session):
    response = api_session.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404

@pytest.mark.parametrize("post_id", [1, 2, 3, 50, 100])
def test_posts_return_200(api_session, post_id):
    response = api_session.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_create_post_returns_201(api_session):
    new_post = {"title": "My Test Post", "body": "Test body content", "userId": 1}
    response = api_session.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My Test Post"

def test_update_post_returns_200(api_session):
    updated = {"title": "Updated Title", "body": "Updated body", "userId": 1}
    response = api_session.put(f"{BASE_URL}/posts/1", json=updated)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

def test_delete_post_returns_200(api_session):
    response = api_session.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200