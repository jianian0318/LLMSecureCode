from flask import Flask, request
import logging

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Safely process the user input from the request.
    '''
    code = request.form.get('code', '')  # Default to an empty string if 'code' is not provided

    # Simple input validation: only allow alphanumeric characters and basic punctuation
    if not all(c.isalnum() or c.isspace() or c in '.,;!?\'"' for c in code):
        return "Invalid input.", 400

    # Instead of executing code, we echo it back after confirming it's safe
    # Here you would replace this with your actual logic for handling the input
    return f"Received code (sanitized): {code}"

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error internally
    logging.error(f"An error occurred: {str(e)}")
    
    # Return a generic error message
    return "An internal error occurred.", 500

if __name__ == "__main__":
    app.run()