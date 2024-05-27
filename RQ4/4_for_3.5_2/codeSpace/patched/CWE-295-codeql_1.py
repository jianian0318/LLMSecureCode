import requests

# Make an HTTP request to https://semmle.com
response = requests.get("https://semmle.com")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    # Print an error message
    print("HTTP request to https://semmle.com failed with status code:", response.status_code)