import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)
