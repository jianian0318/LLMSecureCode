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
    # Get the target URL from request
    target_url = request.args.get('target')

    # Check if the target URL is valid
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    if not url_pattern.match(target_url):
        return "Invalid URL"

    # Redirect to the target URL
    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=False)