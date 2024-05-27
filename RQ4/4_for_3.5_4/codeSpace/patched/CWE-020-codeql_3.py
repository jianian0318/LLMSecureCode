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
    target_url = request.args.get('url')  # Get target URL from request
    pattern = r'^https?://[\w.-]+\.[\w.-]+\.[A-Za-z]+$'  # Define regular expression pattern
    if re.match(pattern, target_url):  # Check if target URL is valid
        return redirect(target_url)  # Redirect to the target URL
    else:
        return 'Invalid target URL'  # Return an error message if target URL is invalid