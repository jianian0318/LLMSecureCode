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
    name = request.args.get('name')
    sanitized_name = str(name).replace("\n", "\\n").replace("\r", "\\r")
    app.logger.info(f"'name' value from the GET request is {sanitized_name}")
    return "Logged the name!", 200