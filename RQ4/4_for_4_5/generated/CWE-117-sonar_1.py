import os
from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    # get the "input" value from the GET request
    input_value = request.args.get('input')

    # check if input_value is not none
    if input_value:
        # log the input_value as an error
        current_app.logger.error('Error: %s', input_value)

    return "Logged Successfully", 200

if __name__ == "__main__":
    debug = os.environ.get("DEBUG_VALUE", False)
    app.run(debug=debug)