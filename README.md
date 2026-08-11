# Automation Booking API

A simple API automation testing project built using Python, Pytest and Requests.

## Technologies Used

- Python
- Pytest
- Requests
- Pytest HTML
- REST API

## API Used

Restful Booker API

Base URL:

https://restful-booker.herokuapp.com

## Project Structure

automation-booking-api/
│
├── tests/
│   ├── test_auth.py
│   ├── test_create_booking.py
│   ├── test_get_booking.py
│   ├── test_update_booking.py
│   ├── test_delete_booking.py
│   ├── test_negative_invalid_booking.py
│   ├── test_negative_invalid_create.py
│   └── test_api_client.py
│
├── utils/
│   ├── api_client.py
│   └── test_data.py
│
├── reports/
│   └── test-report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

## Test Scenarios

The project covers:

1. Authentication
2. Create Booking
3. Get Booking
4. Update Booking
5. Delete Booking
6. Get booking with invalid ID
7. Create booking with invalid data
8. API client GET request

## Setup

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the tests

```bash
pytest
```

### 6. Generate HTML report

```bash
pytest --html=reports/test-report.html
```

## Author

Vishal Mukta
