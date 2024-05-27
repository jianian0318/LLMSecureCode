from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target = request.args.get('url')
    if target:
        # Check if target URL is valid
        if re.match(r'^https?://(www\.)?\w+\.\w+', target):
            return redirect(target)
        else:
            return "Invalid target URL!"
    else:
        return "Target URL not provided!"

if __name__ == '__main__':
    app.run(debug=True)