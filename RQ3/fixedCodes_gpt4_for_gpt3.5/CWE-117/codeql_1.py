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
    Clean it of any potential harmful script or command that could exploit information.
    '''
    name = request.args.get('name')
    cleaned_name = html.escape(name)
    logging.info(cleaned_name)
    return "Logging successful"

if __name__ == '__main__':
    app.run()