from flask import request, current_app, Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)

@app.route('/log', methods=['GET'])
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input_data = request.args.get('input')
    if input_data:
        current_app.logger.error(f'Error: {input_data}')
        return 'Logged the error successfully.', 200
    else:
        return 'No input data provided.', 400