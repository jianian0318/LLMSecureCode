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
    
    target_url = request.args.get('target') # fetching target URL from request

    # using regular expression to check the validity of the URL
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain name
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        # localhost
        r'localhost|'
        # IP
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(url_pattern, target_url) is not None:
        return redirect(target_url)  # redirecting to the target URL
    else:
        return "Invalid URL!", 400 # return a BadRequest status code in case of invalid URL


if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False to prevent Werkzeug debugger exposure