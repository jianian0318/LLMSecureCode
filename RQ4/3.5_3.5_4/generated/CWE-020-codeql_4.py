from flask import Flask, redirect, request
import re
import urllib.parse

app = Flask(__name__)

@app.route('/redirect', methods=['GET', 'POST'])
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    if target_url and checkValidDomain(target_url):
        if 'http://' in target_url or 'https://' in target_url:
            return redirect(target_url)
        else:
            # validate the target_url before redirecting
            target_url = "http://" + target_url
            if checkValidDomain(target_url):
                return redirect(target_url)
    return "Invalid target URL"

def checkValidDomain(url):
    '''
    Check if the provided URL contains a valid domain
    '''
    # Use regular expression to validate the domain
    domain_pattern = '^(https?://)?(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    if re.match(domain_pattern,  url):
        return True
    return False

if __name__ == '__main__':
    app.run()