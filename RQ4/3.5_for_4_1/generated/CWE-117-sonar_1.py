from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input_data = request.args.get('input')  # Gets 'input' from the GET request
    if input_data is not None:
        current_app.logger.error(input_data)  # Logs 'input' as an error
    else:
        return {"message": "No input data provided"}, 400  # Returns an error message if 'input' is not provided
    return {"message": "Input data logged successfully"}, 200  # Returns a success message when 'input' is logged

if __name__ == "__main__":
    app.run(debug=False)  # Running the Flask app without debug mode enabled