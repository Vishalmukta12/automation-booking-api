import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_nonexistent_booking():

    # -------------------------------------------------
    # STEP 1: Use a booking ID that should not exist
    # -------------------------------------------------

    invalid_booking_id = "9900"

    url = f"{BASE_URL}/booking/{invalid_booking_id}"


    # -------------------------------------------------
    # STEP 2: Send GET request
    # -------------------------------------------------

    response = requests.get(url)

    print("Requested Booking ID:", invalid_booking_id)
    print("Status Code:", response.status_code)
    print("Response:", response.text)


    # -------------------------------------------------
    # STEP 3: Verify expected error response
    # -------------------------------------------------

    assert response.status_code == 404

    print("Invalid booking ID handled successfully")