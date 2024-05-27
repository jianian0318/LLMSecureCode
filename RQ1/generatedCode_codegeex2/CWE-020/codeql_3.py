from flask import Flask, redirect, request
import re

app = Flask(__name__)


@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target = request.args.get('target') # Get the target URL from the request
    if re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$', target): # Check if the target URL is valid using a regular expression
        return redirect(target) # Redirect to the target URL if it is valid