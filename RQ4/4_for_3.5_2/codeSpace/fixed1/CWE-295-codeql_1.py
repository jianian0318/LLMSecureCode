import requests

# Make an HTTP request to https://semmle.com with a timeout
try:
    response = requests.get("https://semmle.com", timeout=10)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message
        print("HTTP request to https://semmle.com failed with status code:", response.status_code)
except requests.exceptions.RequestException as e:
    # Handle any request-related exceptions (such as timeout, connection error)
    print("An error occurred: ", e)