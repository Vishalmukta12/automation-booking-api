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

The project is organized as follows:

- **tests/** – Contains all API test cases
  - `test_auth.py` – Authentication test
  - `test_create_booking.py` – Create booking test
  - `test_get_booking.py` – Get booking test
  - `test_update_booking.py` – Update booking test
  - `test_delete_booking.py` – Delete booking test
  - `test_negative_invalid_booking.py` – Invalid booking ID test
  - `test_negative_invalid_create.py` – Invalid booking data test
  - `test_api_client.py` – API client GET test

- **utils/** – Contains reusable utility files
  - `api_client.py` – API request methods
  - `test_data.py` – Test data

- **reports/** – Contains the generated HTML test report

- `conftest.py` – Pytest fixtures
- `pytest.ini` – Pytest configuration
- `requirements.txt` – Python dependencies
- `.gitignore` – Files excluded from Git
- `README.md` – Project documentation

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
