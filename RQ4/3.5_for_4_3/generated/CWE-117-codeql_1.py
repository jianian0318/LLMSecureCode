from flask import Flask, request
import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    # Sanitize the log message by using the `request.formatter()` method
    sanitized_name = app.logger.process(name)
    logger.info('Name: %s', sanitized_name)
    return "Name logged", 200

if __name__ == '__main__':
    app.run()