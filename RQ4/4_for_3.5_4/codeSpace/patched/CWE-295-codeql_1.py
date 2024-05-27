import requests

url = "https://semmle.com"

response = requests.get(url)

print(response.text)