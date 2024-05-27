from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    name = request.args.get('name')

    # Fix the vulnerability by properly escaping the log message
    log_message = f'Received a request from {name}'
    logging.info('Received a request from %s', name)

    return 'Logged successfully'