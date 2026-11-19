import random
import string
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def random_string(length=8):
    chars = string.ascii_lowercase
    return "".join(random.choices(chars, k=length))


test_payload = {
    "id": random.randint(1, 100000),
    "name": random_string(),
    "description": "This is a test item",
    "price": 123.45,
}


def test_create_item():
    # Create item
    response = client.post("/items/", json=test_payload)
    assert response.status_code == 200

    # Check response
    data = response.json()
    assert data["id"] == test_payload["id"]
    assert data["name"] == test_payload["name"]
    assert data["description"] == test_payload["description"]
    assert data["price"] == str(test_payload["price"])
