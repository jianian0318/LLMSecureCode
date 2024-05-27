import requests

response = requests.get('https://semmle.com', timeout=10)
print(response.text)