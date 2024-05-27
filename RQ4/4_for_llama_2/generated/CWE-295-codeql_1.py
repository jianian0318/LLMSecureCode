import requests

try:
    # Make an HTTP request to https://semmle.com with a timeout
    response = requests.get('https://semmle.com', timeout=5)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request successful!')
    else:
        print('Request failed!')

except requests.exceptions.Timeout:
    print('The request timed out')
except requests.exceptions.RequestException as e:
    # handles other types of exceptions
    print('Something went wrong! Error: ', e)