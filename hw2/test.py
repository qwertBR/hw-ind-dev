import pytest
import connexion
import json

flask_app = connexion.FlaskApp(__name__)
flask_app.add_api("swagger.yaml")


@pytest.fixture(scope="module")
def client():
    with flask_app.app.test_client() as c:
        yield c


def test_hello_handler(client):
    response = client.get("api/v1/hello")
    assert response.data == b"Hse One Love!"
    assert response.status_code == 200


def test_set_handler(client):
    response = client.post(
        "api/v1/set",
        data=json.dumps({"key": "key1", "value": "value1"}),
        content_type="application/json",
    )
    assert response.get_data() == b"Ok"
    assert response.status_code == 200

    response = client.post("api/v1/set", data="alexander pistoletov")
    assert response.status_code == 415


def test_get_handler(client):
    client.post(
        "api/v1/set",
        data=json.dumps({"key": "key1", "value": "value1"}),
        content_type="application/json",
    )
    response = client.get("api/v1/get/key1")
    assert response.get_data() == b'["key1","value1"]\n'


def test_divide_handler(client):
    response = client.post(
        "api/v1/divide",
        data=json.dumps({"dividend": 15, "divider": 10}),
        content_type="application/json",
    )
    assert response.get_data() == b"1.5"
    assert response.status_code == 200

    response = client.post("api/v1/divide", data="aleksandr duma")

    assert response.status_code == 415
