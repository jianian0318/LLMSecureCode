import requests

# Make an HTTP request to https://semmle.com with a timeout of 5 seconds
response = requests.get("https://semmle.com", timeout=5)