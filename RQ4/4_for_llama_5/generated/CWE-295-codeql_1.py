import requests

# Make an HTTP request to https://semmle.com
try:
    response = requests.get('https://semmle.com', timeout=5)
except requests.exceptions.Timeout:
    print('The request timed out')
else:
    # Check if the request was successful
    if response.status_code == 200:
        print('Request successful')
    else:
        print('Request failed')