from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger', methods=['GET'])  # add methods=['GET'] to only handle GET requests
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')  # get the "name" value from the GET parameters
    logging.info(name)  # log the name as an information message
    return 'Logged: {}'.format(name)  # return a response to the client