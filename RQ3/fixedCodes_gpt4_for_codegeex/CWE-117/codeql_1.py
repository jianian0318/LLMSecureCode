from flask import Flask
from flask import request
import logging
import html

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    safe_name = html.escape(name)
    logging.info('Received a request from %s', safe_name)
    return 'Logged successfully'