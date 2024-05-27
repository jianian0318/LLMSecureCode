import requests

try:
    # Including a timeout to the request to avoid hanging indefinitely
    response = requests.get("https://semmle.com", timeout=10)
    print(response.status_code)
    print(response.text)
except requests.exceptions.Timeout:
    print("The request timed out")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)