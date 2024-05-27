from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    # Get 'input' from the GET request
    input_data = request.args.get('input')
    
    # log 'input' as an error
    current_app.logger.error('Logging error: %s', input_data)
    
    return 'Logged!', 200  # send a response to the client

# Run the application
if __name__ == "__main__":
    app.run(debug=False)