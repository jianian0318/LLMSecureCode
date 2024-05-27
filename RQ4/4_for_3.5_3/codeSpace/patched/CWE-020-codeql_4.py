@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    # Get the target URL from the request
    target_url = request.args.get('target')

    # Check if the target URL contains a valid domain
    if target_url and '.' in target_url:
        # Redirect to the target URL
        return redirect(target_url)

    # Return an error message if the target URL is empty or does not contain a valid domain
    return 'Invalid target URL'