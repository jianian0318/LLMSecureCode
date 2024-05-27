import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    # Get the subdomain from the request
    subdomain = request.args.get('subdomain')
    
    # Validate input to avoid code injection
    if not subdomain or not subdomain.isalnum():
        return "Invalid subdomain", 400
    
    # Sanitize the subdomain to prevent XSS vulnerability
    sanitized_subdomain = escape(subdomain)
    
    # Validate the sanitized input to ensure it is safe for making HTTP request
    if not sanitized_subdomain.isalnum():
        return "Invalid subdomain", 400
    
    # Use the sanitized subdomain as the url
    url = "http://" + sanitized_subdomain + ".example.com"
    
    try:
        # Make a request to the url with a timeout
        response = requests.get(url, timeout=3)
    except requests.exceptions.RequestException as e:
        # Do not return detailed exception information to external users
        return "Something went wrong", 500
    
    # Return the response
    return response.text

if __name__ == "__main__":
    app.run()