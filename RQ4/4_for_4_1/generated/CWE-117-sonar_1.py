from flask import request, Flask
import logging

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log an error message.
    '''
    input_str = request.args.get('input')
    if input_str:
        # Log the input_str as an error message
        app.logger.error(input_str)
        return 'Logged successfully'
    else:
        return '"input" is not provided in the GET request', 400

if __name__ == '__main__':
    # If not set, the logging level will be WARNING by default. So, it won't log ERRORs and CRITICALs
    app.logger.setLevel(logging.ERROR)
    # If required, add a FileHandler to log to a file
    file_handler = logging.FileHandler('app.log')
    app.logger.addHandler(file_handler)

    # Run the flask application with debug mode turned off
    app.run(debug=False)