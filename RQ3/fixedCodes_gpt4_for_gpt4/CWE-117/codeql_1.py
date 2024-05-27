import html
from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    Sanitize input to prevent log injection.
    '''
    name = html.escape(request.args.get('name', ''))
    app.logger.info('Logging information message: %s', name) 
    return 'Logged the information message', 200

if __name__ == '__main__':
    app.run(debug=True)