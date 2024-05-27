import requests

# Add timeout to requests.get()
try:
    response = requests.get('https://semmle.com', timeout=5)
    # Check if the request was successful
    if response.status_code == 200:
        print('Request successful')
    else:
        print('Request failed')
except requests.exceptions.Timeout:
    print('The request timed out')
except requests.exceptions.RequestException as err:
    print ("Other error occurred: ",err)