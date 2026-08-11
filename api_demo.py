import requests

url = "https://restful-booker.herokuapp.com/booking"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", response.json())