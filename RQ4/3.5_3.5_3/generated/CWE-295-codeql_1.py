import requests

response = requests.get("https://semmle.com", timeout=10)
print(response.status_code)
print(response.text)