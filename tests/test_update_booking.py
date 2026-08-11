import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_update_booking():

    # -------------------------------------------------
    # STEP 1: Authenticate and get token
    # -------------------------------------------------

    auth_url = f"{BASE_URL}/auth"

    auth_payload = {
        "username": "admin",
        "password": "password123"
    }

    auth_response = requests.post(auth_url, json=auth_payload)

    print("Auth Status Code:", auth_response.status_code)
    print("Auth Response:", auth_response.json())

    assert auth_response.status_code == 200
    assert "token" in auth_response.json()

    token = auth_response.json()["token"]

    print("Token received successfully")


    # -------------------------------------------------
    # STEP 2: Create a booking
    # -------------------------------------------------

    create_url = f"{BASE_URL}/booking"

    create_payload = {
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

    create_response = requests.post(
        create_url,
        json=create_payload
    )

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    print("Created Booking ID:", booking_id)


    # -------------------------------------------------
    # STEP 3: Update the booking
    # -------------------------------------------------

    update_url = f"{BASE_URL}/booking/{booking_id}"

    update_payload = {
        "firstname": "VishalUpdated",
        "lastname": "MuktaUpdated",
        "totalprice": 750,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-08-18",
            "checkout": "2026-08-25"
        },
        "additionalneeds": "Lunch"
    }

    headers = {
        "Cookie": f"token={token}",
        "Content-Type": "application/json"
    }

    update_response = requests.put(
        update_url,
        json=update_payload,
        headers=headers
    )

    print("PUT Status Code:", update_response.status_code)
    print("PUT Response:", update_response.json())

    assert update_response.status_code == 200


    # -------------------------------------------------
    # STEP 4: Verify updated data
    # -------------------------------------------------

    updated_booking = update_response.json()

    assert updated_booking["firstname"] == "VishalUpdated"
    assert updated_booking["lastname"] == "MuktaUpdated"
    assert updated_booking["totalprice"] == 750
    assert updated_booking["depositpaid"] is False
    assert updated_booking["bookingdates"]["checkin"] == "2026-08-18"
    assert updated_booking["bookingdates"]["checkout"] == "2026-08-25"
    assert updated_booking["additionalneeds"] == "Lunch"

    print("Booking updated and verified successfully")