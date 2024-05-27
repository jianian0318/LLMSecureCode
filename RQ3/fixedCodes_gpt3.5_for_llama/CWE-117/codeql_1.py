from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    name = request.args.get('name')
    logging.info('Name: %s' % name)
    return 'Name: %s' % name

if __name__ == '__main__':
    app.run()