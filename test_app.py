from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Calculator API!"
    }

def test_calculation_add():
    response = client.post(
        "/calculate",
        json={"operation": "add", "operand1": 5, "operand2": 3}
    )

    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_calculation_subtract():
    response = client.post(
        "/calculate",
        json={"operation": "subtract", "operand1": 5, "operand2": 3}
    )

    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculation_multiply():
    response = client.post(
        "/calculate",
        json={"operation": "multiply", "operand1": 5, "operand2": 3}
    )

    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_calculation_divide():
    response = client.post(
        "/calculate",
        json={"operation": "divide", "operand1": 10, "operand2": 2}
    )

    assert response.status_code == 200
    assert response.json() == {"result": 5}

