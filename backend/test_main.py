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
    "username": random_string(),
    "email": f"{random_string()}@example.com",
    "password": random_string(length=12),
}


def test_create_item():
    # Create item
    response = client.post("/items/", json=test_payload)
    assert response.status_code == 200

    # Check response
    data = response.json()
    assert data["id"] == test_payload["id"]
    assert data["username"] == test_payload["username"]
    assert data["email"] == test_payload["email"]
    assert data["password"] == test_payload["password"]
