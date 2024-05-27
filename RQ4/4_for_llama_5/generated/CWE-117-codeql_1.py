from flask import Flask
from flask import request
import logging
import html

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logger')
def logger():
    name = request.args.get('name')
    safe_name = html.escape(name)
    logging.info('Name: %s', safe_name)
    return 'Logged'

if __name__ == '__main__':
    app.run()