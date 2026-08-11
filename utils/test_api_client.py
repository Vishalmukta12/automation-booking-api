def test_api_client_get(api_client):

    response = api_client.get("/booking/999999")

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    assert response.status_code == 404