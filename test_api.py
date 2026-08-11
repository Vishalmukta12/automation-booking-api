import requests


def test_get_bookings():
    url = "https://restful-booker.herokuapp.com/booking"

    response = requests.get(url)

    assert response.status_code == 200