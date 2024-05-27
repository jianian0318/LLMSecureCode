from flask import request, current_app, Flask
import html

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input = request.args.get('input')
    html_input = html.escape(input)
    current_app.logger.error(html_input)
    return "Logged: " + html_input