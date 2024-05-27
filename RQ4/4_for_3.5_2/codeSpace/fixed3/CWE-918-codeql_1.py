import requests
from flask import Flask, request, Response
import logging
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# Configure a safe logger that avoids user input
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sanitize_log_message(message):
    """Sanitize the log message to prevent log injection."""
    return message.translate(str.maketrans({
        '\n': r'\n',
        '\r': r'\r',
        '"': r'\"',
        "'": r"\'"
    }))

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request, validate it, and use it as the URL to make a request with a timeout.
    Return the response content safely.
    '''
    subdomain = request.args.get('subdomain')
    allowed_domains = ['example.com', 'api.example.com', 'secure.example.com']
    if subdomain is not None:
        # Validate the subdomain
        if not any(subdomain.endswith(allowed_domain) for allowed_domain in allowed_domains):
            return Response("Invalid subdomain.", status=400)

        url = f"http://{subdomain}"
        # Verify the URL
        parsed_url = urlparse(url)
        if not (parsed_url.scheme and parsed_url.netloc):
            return Response("Malformed URL.", status=400)
        
        # Ensure that the URL is safe (not allowing redirects to unexpected domains)
        if urljoin(url, '/') not in map(lambda domain: f"http://{domain}/", allowed_domains):
            return Response("URL is not allowed.", status=400)

        try:
            response = requests.get(url, timeout=5)
            return Response(response.content, mimetype='text/plain')
        except requests.exceptions.RequestException as e:
            # Log the error safely
            sanitized_message = sanitize_log_message(f"Failed to fetch URL {url}: {str(e)}")
            logger.error(sanitized_message)
            return Response("Failed to retrieve data.", status=504)

    return Response("Subdomain not found in the request parameters", status=400)

if __name__ == "__main__":
    # Disable debug mode for production
    app.run(debug=False)