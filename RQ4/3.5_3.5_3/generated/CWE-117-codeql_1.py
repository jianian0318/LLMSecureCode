from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')  # Get the value of the "name" parameter from the request
    
    if name is not None:
        logging.info('Received name: %s', escape(name))  # Log the name as an information message
        return 'Name logged successfully'
    else:
        logging.warning('Missing name parameter')  # Log a warning if the name parameter is missing
        return 'Missing name parameter'