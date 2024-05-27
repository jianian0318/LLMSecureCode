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
    name_value = request.args.get('name', default = "", type = str)
    app.logger.info('Name Value: %s', repr(name_value))
    return "Logged the name value", 200