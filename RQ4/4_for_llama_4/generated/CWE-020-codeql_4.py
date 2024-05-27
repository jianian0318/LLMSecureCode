from flask import Flask, redirect, request
import validators

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    # Get the target URL from the request
    target_url = request.args.get('target')

    # Check if the target URL is a valid
    if target_url and validators.url(target_url):
        # Redirect to the target URL
        return redirect(target_url)
    else:
        # Return an error message if the target URL is invalid
        return "Invalid target URL"

if __name__ == '__main__':
    # It is important to never run a Flask application in debug mode in a production environment. 
    # Debug mode should only be enabled when developing locally!
    app.run(debug=False)