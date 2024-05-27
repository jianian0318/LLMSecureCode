import requests

# Make an HTTP request to https://semmle.com
try:
    response = requests.get('https://semmle.com', timeout=1.0)
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.TooManyRedirects:
    print("Too many redirects!")
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)