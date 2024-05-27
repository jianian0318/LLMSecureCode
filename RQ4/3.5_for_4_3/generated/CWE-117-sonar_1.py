from flask import request, current_app, Flask
import logging
from html import escape
import re

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    # Get the "input" parameter from the GET request
    input_string = request.args.get('input', '')
    # Escape user input to prevent XSS attack
    input_string = escape(input_string)

    # Validate user input before logging
    if re.match(r'^[a-zA-Z0-9\s]+$', input_string):
        # Configure the logger
        logger = logging.getLogger(__name__)
        # Log the input as an error using logger.error() instead of string concatenation
        logger.error('Logged: %s as an error', input_string)
        return f'Logged: {input_string} as an error'
    else:
        return 'Invalid input provided'

if __name__ == "__main__":
    app.run()