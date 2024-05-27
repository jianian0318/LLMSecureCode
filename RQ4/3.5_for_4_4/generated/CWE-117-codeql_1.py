from flask import Flask
from flask import request
import logging
import html

# Set up logging and disable debug mode
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/logger', methods=['GET'])
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    if name:
        name = html.escape(name)  # Fixing CWE-79 vulnerability by escaping HTML characters

        # Fixing CWE-117 vulnerability by using a logger object to build log entries
        logger = logging.getLogger(__name__)
        logger.info('Information message: %s', name)
    else:
        logger = logging.getLogger(__name__)
        logger.info('No name value in the request')

    return 'Logged name: {}'.format(html.escape(name) if name else 'No name')  # Fixing CWE-79 vulnerability by escaping HTML characters

if __name__ == '__main__':
    app.run()