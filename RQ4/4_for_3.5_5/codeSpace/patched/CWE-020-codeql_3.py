from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():

    # Get target URL from request
    target_url = request.args.get('target')

    # Use a regular expression to check if it is a valid target
    if not re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$', target_url):
        return "Invalid target URL"

    # Redirect to the target URL
    return redirect(target_url)