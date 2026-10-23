from fastapi.testclient import TestClient
# Adjust the import based on how your FastAPI instance is named in main.py
from backend.main import app

client = TestClient(app)

def test_read_root():
  response = client.get("/")
  # Check that your app responds (adjust status code to 200 or whatever your route returns)
  assert response.status_code == 200
