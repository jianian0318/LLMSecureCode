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
    sanitized_name = html.escape(name)
    logging.info(sanitized_name)
    return "Logging successful"

if __name__ == '__main__':
    app.run()