from flask import Flask, request, escape
import requests

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request, validate it, ensure it's a safe request, and return the sanitized response.
    '''
    subdomain = request.args.get('subdomain') # Get the subdomain parameter from the request
    safe_subdomains = {'allowed1','allowed2','allowed3'} # List of allowed subdomains

    if subdomain is None:
        return "Subdomain is missing", 400 # Return an error if subdomain parameter is missing
    
    if subdomain not in safe_subdomains:
        return "Access to the subdomain is not allowed", 403 # Block SSRF by validating subdomains

    url = f"http://{escape(subdomain)}.example.com" # Construct the URL by appending subdomain to the base URL

    try:
        response = requests.get(url, timeout=5) # Make a GET request to the constructed URL with a timeout
        return escape(response.text) # Use escape to prevent XSS by escaping HTML special characters
    except requests.exceptions.RequestException:
        return "An error occurred while fetching data", 500 # Don't reveal internal exception details

if __name__ == "__main__":
    app.run()