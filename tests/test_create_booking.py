import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking():
    url = f"{BASE_URL}/booking"

    payload = {
        "firstname": "Vishal",
        "lastname": "Mukta",
        "totalprice": 500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-15",
            "checkout": "2026-08-20"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    response_data = response.json()

    assert "bookingid" in response_data
    assert "booking" in response_data

    assert response_data["booking"]["firstname"] == "Vishal"
    assert response_data["booking"]["lastname"] == "Mukta"
    assert response_data["booking"]["totalprice"] == 500
    assert response_data["booking"]["depositpaid"] is True