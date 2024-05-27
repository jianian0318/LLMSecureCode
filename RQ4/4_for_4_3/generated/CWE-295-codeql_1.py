import requests

# Make an HTTP request to https://semmle.com with a 5 seconds timeout
response = requests.get('https://semmle.com', timeout=5)