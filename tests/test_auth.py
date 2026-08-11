import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_authentication(auth_token):
    assert auth_token is not None
    assert len(auth_token) > 0