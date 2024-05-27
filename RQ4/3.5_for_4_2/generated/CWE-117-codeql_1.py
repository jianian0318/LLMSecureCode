from flask import Flask
from flask import request
import logging
from markupsafe import escape

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = escape(request.args.get('name'))  # Get the "name" value from the GET request and escape it.
    logging.info("Name: {}".format(name))  # Log the "name" value as an information message.
    return "Logged: {}".format(name)  # Return a response to the client.

if __name__ == "__main__":
    app.run()