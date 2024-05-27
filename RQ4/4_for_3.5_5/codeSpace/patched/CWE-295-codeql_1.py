import requests

response = requests.get('https://semmle.com')

response.raise_for_status()

print(response.text)