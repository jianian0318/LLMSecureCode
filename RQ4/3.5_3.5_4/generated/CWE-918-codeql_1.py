import requests

@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get("subdomain")  # Get the subdomain from the request's query parameters
    url = f"https://{subdomain}.example.com"  # Construct the URL using the subdomain
    response = requests.get(url, timeout=5)  # Make a GET request to the URL with a timeout of 5 seconds
    return response.text  # Return the response's content as the HTTP response