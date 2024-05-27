from flask import request, current_app, Flask
import html

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log():
    input_data = request.args.get('input')
    input_data = html.escape(input_data) # Fix CWE-117 vulnerability by HTML escaping
    current_app.logger.error(input_data)

    return 'Logged the input data as error.'