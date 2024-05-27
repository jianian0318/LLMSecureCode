from flask import Flask, request, escape
import logging

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Safely process the user input from the request by escaping HTML entities.
    '''
    code = request.form.get('code', '')  # Default to an empty string if 'code' is not provided

    # Simple input validation: only allow alphanumeric characters and basic punctuation
    if not all(c.isalnum() or c.isspace() or c in '.,;!?\'"' for c in code):
        return "Invalid input.", 400

    # Escape HTML special characters in the user input to prevent XSS
    code_sanitized = escape(code)

    # Instead of executing code, we echo it back after confirming it's safe
    # Here you would replace this with your actual logic for handling the input
    return f"Received code (sanitized): {code_sanitized}"

@app.errorhandler(Exception)
def handle_exception(e):
    # Log the error internally
    logging.error(f"An error occurred: {str(e)}")
    
    # Return a generic error message
    return "An internal error occurred.", 500

if __name__ == "__main__":
    # Ensure that you do not run the app with debug=True in production to avoid vulnerabilities
    app.run(debug=False)