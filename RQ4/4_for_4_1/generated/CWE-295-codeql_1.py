import requests

# Define a timeout value (e.g. 5 seconds)
timeout = 5

# Make an HTTP request to https://semmle.com
try:
    response = requests.get('https://semmle.com', timeout=timeout)
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.RequestException as err:
    print ("Unexpected Error:",err)
else:
    print(response)