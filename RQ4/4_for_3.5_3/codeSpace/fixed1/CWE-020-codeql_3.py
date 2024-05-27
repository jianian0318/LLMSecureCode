from flask import Flask, redirect, request, url_for
import re

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request,
    validate it using a regular expression to ensure it's a valid and safe target,
    then redirect to the target URL only if the validation is successful.
    '''
    target = request.args.get('url')
    if target:
        # Validate the target URL by checking it against a pattern
        # Ensure it does not allow redirection to arbitrary websites
        if re.match(r'^https?://(www\.)?example\.com/', target):
            return redirect(target)
        else:
            return "Invalid or disallowed target URL!"
    else:
        return "Target URL not provided!"

# Main execution
if __name__ == '__main__':
    # Set debug to False in deployment. For development, it can be set to True if needed.
    # However, always ensure to switch it off when deploying.
    app.run(debug=False)