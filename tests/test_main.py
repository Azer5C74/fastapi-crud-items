# tests/test_main.py
import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def sample_item():
    return {"name": "Test Item"}

def test_read_root():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_item(sample_item):
    response = requests.post(f"{BASE_URL}/items/", json=sample_item)
    assert response.status_code == 200
    assert response.json()["message"] == "Item created successfully"

def test_read_items():
    response = requests.get(f"{BASE_URL}/items/")
    assert response.status_code == 200
    assert "items" in response.json()