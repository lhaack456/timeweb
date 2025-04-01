import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as app_client:
        yield app_client

def test_main(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Current Date and Time:" in response.data

def test_time(client):
    response = client.get('/')
    assert b"," in response.data
