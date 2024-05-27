@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    subdomain = request.args.get('subdomain') # Get the subdomain parameter from the request
    
    if subdomain is None:
        return "Subdomain is missing", 400 # Return an error if subdomain parameter is missing
    
    url = f"http://{subdomain}.example.com" # Construct the URL by appending subdomain to the base URL
    
    try:
        response = requests.get(url) # Make a GET request to the constructed URL
        return response.text # Return the response content as the result
    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500 # Return an error if there is an exception during the request