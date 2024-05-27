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
    target_url = request.args.get('url')

    if target_url is None:
        return 'No target URL provided'

    if re.match(r'^https?://(?:www\.)?\w+\.\w{2,3}$', target_url):
        return redirect(target_url)
    else:
        return 'Invalid target URL'