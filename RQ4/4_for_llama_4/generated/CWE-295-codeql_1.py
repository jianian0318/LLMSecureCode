import requests

# Set the timeout for the request (in seconds)
TIMEOUT = 10

try:
    # Make an HTTP request to https://semmle.com with a timeout
    response = requests.get('https://semmle.com', timeout=TIMEOUT)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request successful')
    else:
        print('Request failed with status code:', response.status_code)
except requests.Timeout:
    # The request timed out
    print('The request timed out after', TIMEOUT, 'seconds')
except requests.RequestException as e:
    # Handle other possible exceptions (like network issues)
    print('An error occurred:', str(e))