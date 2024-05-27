import requests

response = requests.get("https://semmle.com")

print(response.status_code)
print(response.text)