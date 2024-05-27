import logging
from flask import request, current_app, Flask
import html

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)

@app.route('/log', methods=['GET'])
def log():
    input_data = request.args.get('input')
    sanitized_data = html.escape(input_data) #sanitize input for logging
    current_app.logger.error(sanitized_data)

    return 'Logged the input data as error.'

if __name__ == "__main__":
    app.run()