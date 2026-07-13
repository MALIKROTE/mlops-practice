##### Week 5 - Day 2 #####
##### FastAPI Unit Testing using pytest #####

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "PyTorch Prediction API"
    }


def test_prediction():
    response = client.post(
        "/predict",
        json={
            "value": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["input"] == 5

    assert "prediction" in data

    assert isinstance(data["prediction"], float)