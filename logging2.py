import logging

# Configure logging
logging.basicConfig(
    filename='web_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def login(username):
    logging.info(f"User {username} logged in")
    # Simulate login processing

def process_data(data):
    try:
        # Simulate data processing
        if data == "bad_data":
            raise ValueError("Invalid data")
        logging.info(f"Data processed: {data}")
    except ValueError as e:
        logging.error(f"Error processing data: {e}", exc_info=True)

def logout(username):
    logging.info(f"User {username} logged out")
    # Sim


if __name__ == "__main__":
    user_name = "Ananth Sagar"
    login(user_name)
    process_data("bad_data")
    logout(user_name)


import pytest

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(10, 0)
