import logging
from logging.handlers import RotatingFileHandler
from flask import request, Flask

app = Flask(__name__)
app.debug = False  # ensure debug mode is turned off

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
logging_format = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler.setFormatter(logging_format)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and securely log it.
    '''
    # Extract "input" from GET request.
    input_data = request.args.get('input', type=str)  # Ensure input_data is a string to prevent type juggling attacks.
    
    # If "input" is present, sanitize it and log it securely.
    if input_data is not None:
        sanitized_data = ''.join(e for e in input_data if e.isalnum() or e.isspace())  # Sanitize input (keep alphanumeric and spaces) to prevent malicious log entry.
        # Use properly parameterized logging to prevent log forging.
        app.logger.info('Received user input: %s', sanitized_data)

    return 'Logged securely.', 200

if __name__ == '__main__':
    app.run(debug=False)  # ensure debug mode is turned off