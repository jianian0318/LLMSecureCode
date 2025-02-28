from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('target_url') # Get the target URL from the request
    if is_valid_domain(target_url): # Check if the target URL contains a valid domain
        return redirect(target_url) # Redirect to the target URL if it is valid