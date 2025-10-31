import requests

def check_internet_connection():
    try:
        # Try to make a GET request to a known website
        response = requests.get("https://www.google.com")
        # If the response status code is 200, it means the request was successful
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def check_internet():
    if check_internet_connection():
        return True
    else:
        return False
