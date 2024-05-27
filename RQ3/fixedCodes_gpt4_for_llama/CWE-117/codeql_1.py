from flask import Flask
from flask import request
import logging
from html import escape

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    safe_name = escape(name)
    logging.info(f'Name: {safe_name}')
    return f'Name: {safe_name}'

if __name__ == '__main__':
    app.run()