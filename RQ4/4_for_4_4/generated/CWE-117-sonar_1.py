from flask import request, Flask
import logging
import html

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/log')
def log_data():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input_value = request.args.get("input", None)
    if input_value is not None:
        # Sanitize the input value using the html.escape method from the html module
        sanitized_input = html.escape(input_value)
        log.error("Error: %s", sanitized_input)
    else:
        return 'No input found'
    return 'Logged successfully'

if __name__ == "__main__":
    app.run(debug=False)