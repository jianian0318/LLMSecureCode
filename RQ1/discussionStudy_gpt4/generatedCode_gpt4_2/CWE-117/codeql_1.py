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
    name = request.args.get("name")
    logging.info('Name value: %s' % name)
    return 'Logged Name', 200

if __name__ == '__main__':
    app.run(debug=True)