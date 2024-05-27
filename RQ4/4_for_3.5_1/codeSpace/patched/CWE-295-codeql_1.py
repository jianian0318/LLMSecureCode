import requests

# Make an HTTP request to https://semmle.com
response = requests.get("https://semmle.com")

# Print the status code of the response
print(response.status_code)