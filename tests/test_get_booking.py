import requests
import time

BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_booking():
    # Step 1: Create a booking
    create_url = f"{BASE_URL}/booking"

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

    create_response = requests.post(create_url, json=payload)

    print(f"Create Status Code: {create_response.status_code}")
    print(f"Create Response: {create_response.text}")

    # Verify booking was created
    assert create_response.status_code in [200, 201]

    create_data = create_response.json()

    booking_id = create_data["bookingid"]

    print(f"Created Booking ID: {booking_id}")

    # Step 2: Get the booking
    get_url = f"{BASE_URL}/booking/{booking_id}"

    get_response = None

    # Retry because the public demo API can occasionally take
    # a moment before the newly created booking is available.
    for attempt in range(3):
        get_response = requests.get(get_url)

        print(
            f"GET Attempt {attempt + 1} - "
            f"Status Code: {get_response.status_code}"
        )

        if get_response.status_code == 200:
            break

        time.sleep(2)

    # Step 3: Verify GET response
    assert get_response.status_code == 200

    get_data = get_response.json()

    print(f"GET Response: {get_data}")

    # Step 4: Verify booking details
    assert get_data["firstname"] == "Vishal"
    assert get_data["lastname"] == "Mukta"
    assert get_data["totalprice"] == 500
    assert get_data["depositpaid"] is True
    assert get_data["bookingdates"]["checkin"] == "2026-08-15"
    assert get_data["bookingdates"]["checkout"] == "2026-08-20"
    assert get_data["additionalneeds"] == "Breakfast"

    print("Booking retrieved and verified successfully")