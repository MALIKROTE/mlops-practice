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

    ##### Week 5 - Day 3 #####
##### Testing Invalid Requests #####


def test_prediction_missing_value():

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 422


def test_prediction_invalid_type():

    response = client.post(
        "/predict",
        json={
            "value": "hello"
        }
    )

    assert response.status_code == 422


def test_prediction_null_value():

    response = client.post(
        "/predict",
        json={
            "value": None
        }
    )

    assert response.status_code == 422

def test_prediction_negative_number():

    response = client.post(
        "/predict",
        json={
            "value": -5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data["prediction"], float)