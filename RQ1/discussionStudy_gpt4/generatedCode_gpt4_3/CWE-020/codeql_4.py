from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target = request.args.get('target')
    validate = re.match(r'http[s]?:\/\/[a-z0-9-]+\.[a-z0-9-.]+', target)

    if validate:
        return redirect(target, code=302)
    else:
        return 'Invalid URL'


if __name__ == "__main__":
    app.run(port=8080)