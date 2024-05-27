import logging
from flask import request, current_app, Flask
import html

app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route('/log')
def log():
    input = request.args.get('input')
    sanitized_input = html.escape(input)
    current_app.logger.error(sanitized_input)
    return 'Logged successfully'

if __name__ == '__main__':
    app.run()