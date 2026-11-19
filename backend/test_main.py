import random
import string
from fastapi.testclient import TestClient
from backend.main import app


client = TestClient(app)


def random_string(length=8):
    chars = string.ascii_lowercase
    return "".join(random.choices(chars, k=length))


test_payload = {
    "name": random_string(),
    "description": "This is a test item",
    "price": 123.45,
}


def test_create_item():
    # Create item
    response = client.post("/items", json=test_payload)
    assert response.status_code == 200

    # Check response
    data = response.json()
    assert data["name"] == test_payload["name"]
    assert data["description"] == test_payload["description"]
    assert data["price"] == str(test_payload["price"])
