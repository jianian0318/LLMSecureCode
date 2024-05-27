import requests

# URL to the website
url = 'https://semmle.com'

# Set a timeout for the request (e.g., 10 seconds)
timeout = 10

try:
    # Making a GET request with timeout
    response = requests.get(url, timeout=timeout)

    # Print the status code
    print(response.status_code)
except requests.exceptions.Timeout:
    # Handle timeout error
    print("Request timed out")
except requests.exceptions.RequestException as e:
    # Handle other request-related errors
    print("An error occurred:", e)