from utils.api_client import APIClient


BASE_URL = "https://restful-booker.herokuapp.com"


def test_api_client_get():

    client = APIClient(BASE_URL)

    response = client.get("/booking/999999")

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    assert response.status_code == 404