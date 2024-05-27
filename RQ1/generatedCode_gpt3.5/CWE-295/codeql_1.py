import requests

# Make an HTTP GET request to https://semmle.com
response = requests.get("https://semmle.com")

# Print the response text
print(response.text)