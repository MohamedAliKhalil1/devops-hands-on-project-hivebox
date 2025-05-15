from fastapi.testclient import TestClient 
from main import app


client = TestClient(app)

def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200
    data = response.json()
    assert "version" in data
    assert isinstance(data["version"], str)