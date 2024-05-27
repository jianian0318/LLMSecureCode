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
    # get target URL from request
    target = request.args.get('url')

    # use a regular expression to check if it is a valid target
    validation = re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', target)

    # check if the validation is not None (i.e. target is valid)
    if validation is not None:
        # redirect to the target URL
        return redirect(target)
    else:
        return "Invalid URL"

if __name__ == "__main__":
    app.run(debug=True)