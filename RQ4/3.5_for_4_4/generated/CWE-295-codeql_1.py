import requests

# Make an HTTP request to https://semmle.com with a timeout of 10 seconds
response = requests.get('https://semmle.com', timeout=10)

# You can then check the status of your request using response.status_code
print("Response Status Code: ", response.status_code)