import requests

# Define a reasonable timeout duration
TIMEOUT_DURATION = 10  # seconds

try:
    response = requests.get('https://semmle.com', timeout=TIMEOUT_DURATION)
    response.raise_for_status()
    print(response.text)
except requests.RequestException as e:
    print(f"An error occurred: {e}")