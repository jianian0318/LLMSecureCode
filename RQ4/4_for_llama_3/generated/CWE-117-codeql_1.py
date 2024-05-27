from flask import Flask
from flask import request
import logging
import html

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def sanitize_input(input):
    return html.escape(input)

@app.route('/logger')
def logger():
    name = sanitize_input(request.args.get('name'))
    logging.info(f'Name: {name}')
    return 'Logging successful'

if __name__ == '__main__':
    app.run()