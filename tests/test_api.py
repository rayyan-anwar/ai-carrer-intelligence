from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_match_api():
    response = client.post("/api/v1/match", json={
        "resume": "Python machine learning SQL and Docker experience",
        "job_description": "Python machine learning engineer with SQL and Docker"
    })
    assert response.status_code == 200
    assert "score" in response.json()
