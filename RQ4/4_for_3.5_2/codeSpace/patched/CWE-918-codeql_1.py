@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain')
    if subdomain is not None:
        url = f"http://{subdomain}" # Add the protocol "http://" to the subdomain
        response = requests.get(url)
        return response.text
    else:
        return "Subdomain not found in the request parameters"