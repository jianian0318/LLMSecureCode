from flask import request, current_app, Flask
import html

app = Flask(__name__)
@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input_data = request.args.get('input')
    sanitized_data = html.escape(input_data)
    current_app.logger.error(sanitized_data)
    return "Logged as an error"