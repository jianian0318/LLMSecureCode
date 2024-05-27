from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    # Get the "name" value from the GET request
    name = request.args.get('name')
    # Log it as an information message
    app.logger.info('Name is %s', name)
    return 'Logged the name successfully', 200

if __name__=='__main__':
    app.run(debug=True)