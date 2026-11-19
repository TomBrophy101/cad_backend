def test_create_item():
    # Create item
    response = client.post("/items", json=test_payload)
    assert response.status_code == 200
    #
    # Check response
    data = response.json()
    assert data["name"] == test_payload["name"]
    assert data["description"] == test_payload["description"]
    assert data["price"] == str(test_payload["price"])

test_payload = {
    "name": random_string(),
    "description": "This is a test item",
    "price": 123.45
}
