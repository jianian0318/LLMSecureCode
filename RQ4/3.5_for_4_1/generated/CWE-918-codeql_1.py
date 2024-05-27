import requests
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, 
    make a request to the url, and return the response
    '''
    # Parse subdomain from the request
    subdomain = request.args.get('subdomain')

    # Check if subdomain exists
    if subdomain:
        # Sanitize subdomain input
        sanitized_subdomain = escape(subdomain)

        # Define the URL using the sanitized subdomain
        url = f"http://{sanitized_subdomain}.example.com"
        
        try:
            # Make a request to the URL with timeout
            response = requests.get(url, timeout=5)

            # Sanitize response content
            sanitized_response = escape(response.content)

            # Return the sanitized response content as a string
            return sanitized_response

        except requests.exceptions.Timeout:
            return "Request timed out"

    else:
        return "No subdomain provided in the request"