from flask import Flask, request
import logging
import html

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/logger', methods=['GET'])
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name', '')
    if name:
        sanitized_name = sanitize_input(name)
        app.logger.info("Received name: %s", sanitized_name)
    else:
        app.logger.warning("No name provided")
    return "Logged the name"

def sanitize_input(input_string):
    '''
    Sanitize the input by removing special characters and escaping any HTML entities.
    '''
    sanitized_string = html.escape(input_string)
    return sanitized_string

if __name__ == "__main__":
    app.run()