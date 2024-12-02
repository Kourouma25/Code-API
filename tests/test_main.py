import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Bienvenue sur l'API de prédiction bancaire"}

def test_prediction(client):
    payload = {"feature1": 1.0, "feature2": 2.0}  # Adapter selon vos données
    response = client.post("/predire", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json.get("resultats", {})
