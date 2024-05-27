import requests

# Make an HTTP request to https://semmle.com with a timeout of 5 seconds
try:
    response = requests.get('https://semmle.com', timeout=5)
except requests.exceptions.Timeout:
    print('The request timed out')
except requests.exceptions.TooManyRedirects:
    print('Too many redirects')
except requests.exceptions.RequestException as e:
    print('There was an ambiguous exception that occurred while handling your request.', e)