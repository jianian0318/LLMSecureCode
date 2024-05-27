import requests

url = "https://semmle.com"

# Adding a timeout to the requests.get call to prevent hanging indefinitely
timeout_duration = 10  # Timeout set to 10 seconds
response = requests.get(url, timeout=timeout_duration)

print(response.text)