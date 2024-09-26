from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_read_main(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
