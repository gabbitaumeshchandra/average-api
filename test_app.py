
import pytest
from app import app, numbers


@pytest.fixture(autouse=True)
def clear_numbers():
    """Start each test with an empty list."""
    numbers.clear()
    yield
    numbers.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_first_number(client):
    response = client.post("/average", json=10)

    assert response.status_code == 200
    assert response.get_json()["average"] == 10


def test_running_average(client):
    client.post("/average", json=10)
    response = client.post("/average", json=20)

    assert response.get_json()["average"] == 15


def test_decimal_numbers(client):
    client.post("/average", json=1.5)
    response = client.post("/average", json=2.5)

    assert response.get_json()["average"] == 2


def test_negative_numbers(client):
    client.post("/average", json=-10)
    response = client.post("/average", json=20)

    assert response.get_json()["average"] == 5


def test_invalid_input(client):
    response = client.post("/average", json="hello")

    assert response.status_code == 400


def test_missing_number(client):
    response = client.post("/average", json={})

    assert response.status_code == 400


def test_invalid_input_does_not_change_average(client):
    client.post("/average", json=10)
    client.post("/average", json="hello")
    response = client.post("/average", json=20)

    assert response.get_json()["average"] == 15


def test_non_json_request(client):
    response = client.post(
        "/average",
        data="10",
        content_type="text/plain"
    )

    assert response.status_code == 415
