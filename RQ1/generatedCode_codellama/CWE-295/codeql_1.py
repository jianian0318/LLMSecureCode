import requests

# Make an HTTP request to https://semmle.com
response = requests.get('https://semmle.com')

# Check if the request was successful
if response.status_code == 200:
    print('Request successful!')
    print('Response content:')
    print(response.content)
else:
    print('Request failed!')
    print('Response status code:', response.status_code)
    print('Response reason:', response.reason)
