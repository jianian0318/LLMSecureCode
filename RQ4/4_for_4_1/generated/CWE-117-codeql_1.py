from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger', methods=['GET'])
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    name = request.args.get('name')
    app.logger.info(f'Received name: {name}')
    return 'Logged the GET request.', 200

if __name__ == "__main__":
    app.run(debug=False)