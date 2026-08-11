import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking_with_invalid_data():

    # -------------------------------------------------
    # STEP 1: Create an invalid booking payload
    # -------------------------------------------------

    invalid_payload = {
        "firstname": "",
        "lastname": "",
        "totalprice": "invalid",
        "depositpaid": "invalid",
        "bookingdates": {}
    }


    # -------------------------------------------------
    # STEP 2: Send POST request
    # -------------------------------------------------

    url = f"{BASE_URL}/booking"

    response = requests.post(
        url,
        json=invalid_payload
    )

    print("Status Code:", response.status_code)
    print("Response:", response.text)


    # -------------------------------------------------
    # STEP 3: Verify API response
    # -------------------------------------------------

    assert response.status_code != 200

    print("Invalid booking data handled successfully")