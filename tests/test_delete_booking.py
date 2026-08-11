import requests


BASE_URL = "https://restful-booker.herokuapp.com"


def test_delete_booking():

    # -------------------------------------------------
    # STEP 1: Authenticate and get token
    # -------------------------------------------------

    auth_url = f"{BASE_URL}/auth"

    auth_payload = {
        "username": "admin",
        "password": "password123"
    }

    auth_response = requests.post(
        auth_url,
        json=auth_payload
    )

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

    print("Create Status Code:", create_response.status_code)
    print("Create Response:", create_response.json())

    assert create_response.status_code == 200

    booking_id = create_response.json()["bookingid"]

    print("Created Booking ID:", booking_id)


    # -------------------------------------------------
    # STEP 3: Delete the booking
    # -------------------------------------------------

    delete_url = f"{BASE_URL}/booking/{booking_id}"

    headers = {
        "Cookie": f"token={token}"
    }

    delete_response = requests.delete(
        delete_url,
        headers=headers
    )

    print("DELETE Status Code:", delete_response.status_code)
    print("DELETE Response:", delete_response.text)

    assert delete_response.status_code == 201

    print("Booking deleted successfully")


    # -------------------------------------------------
    # STEP 4: Verify the booking has been deleted
    # -------------------------------------------------

    get_response = requests.get(delete_url)

    print("GET After DELETE Status Code:", get_response.status_code)

    assert get_response.status_code == 404

    print("Booking deletion verified successfully")