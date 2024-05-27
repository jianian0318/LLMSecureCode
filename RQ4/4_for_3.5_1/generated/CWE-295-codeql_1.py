import requests

# Make an HTTP request to https://semmle.com with a timeout of 5 seconds
response = requests.get("https://semmle.com", timeout = 5)

# Print the status code of the response
print(response.status_code)