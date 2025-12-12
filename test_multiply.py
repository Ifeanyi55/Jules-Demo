from fastapi.testclient import TestClient
from multiply import app

client = TestClient(app)

def test_multiply_numbers():
    response = client.post("/multiply", json={"a": 5, "b": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 50}
