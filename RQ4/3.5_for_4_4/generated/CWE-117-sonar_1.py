from flask import request, current_app, Flask
import logging
import html

app = Flask(__name__)
app.logger.setLevel(logging.ERROR)

@app.route('/log')
def log():
    input_data = request.args.get('input')  # Get the "input" from the GET request

    # Sanitize user input to prevent forged log entries
    sanitized_input = html.escape(input_data)

    # Log the error using Flask's built-in logging
    app.logger.error('Error logged: %s', sanitized_input)

    return f'Logged error: {sanitized_input}'

if __name__ == "__main__":
    app.run()