from flask import request, current_app, Flask, escape

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/log')
def log_message():
    # Get the "input" from the GET request
    input_message = request.args.get('input', '')

    # Log it as an error using Flask's logger
    current_app.logger.error('Error logged: %s', escape(input_message))  # Escaping user input to prevent cross-site scripting

    return f"Logged message: {escape(input_message)}"  # Escaping user input to prevent cross-site scripting

if __name__ == '__main__':
    app.run()