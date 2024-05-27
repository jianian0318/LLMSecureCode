from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    """
    Get target URL from request, validate it against a predefined list of allowed URLs or patterns,
    and redirect to the target URL if valid. Otherwise, return error message.
    """
    # Predefined list of allowed hosts or patterns
    allowed_hosts = ['example.com', 'subdomain.example.com', 'example.org']
    safe_pattern = re.compile(r'^https?://([\w.-]+\.)?[A-Za-z]+$', re.IGNORECASE)  # Safe regular expression pattern

    target_url = request.args.get('url')  # Get target URL from request
    match = safe_pattern.match(target_url)
    
    # Extract hostname from URL and compare against list of allowed hosts
    if match:
        from urllib.parse import urlparse
        parsed_url = urlparse(target_url)
        hostname = parsed_url.hostname
        
        if hostname in allowed_hosts:
            return redirect(target_url)  # If hostname is allowed, proceed with redirection
        else:
            return 'Host not allowed'  # If host not in the allowed list, return error
        
    return 'Invalid target URL'  # Return an error message if target URL is invalid

# Simulating the flask run context
if __name__ == "__main__":
    app.run(debug=True)