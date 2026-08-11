import pytest
import requests

from utils.api_client import APIClient


@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture
def auth_token(base_url):
    auth_url = f"{base_url}/auth"

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(auth_url, json=payload)

    assert response.status_code == 200

    token = response.json()["token"]

    return token


@pytest.fixture
def api_client(base_url):
    return APIClient(base_url)