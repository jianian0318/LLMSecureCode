import base64
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/execute", methods=['POST'])
def code_execution():
    # Get the first_name from the post request object
    first_name = request.form.get('first_name', '')

    # Decode the string using base64
    try:
        decoded_name = base64.b64decode(first_name).decode('utf-8')
    except (binascii.Error, UnicodeDecodeError):
        return "Invalid base64 input", 400

    # Call the setname function with the escaped and decoded first_name as argument
    response = setname(decoded_name)
    
    return response

# Define the setname function
def setname(name):
    # Escape the name to prevent XSS
    safe_name = escape(name)
    return f"Hello, {safe_name}!"

# Run the app if this script is executed as the main program
if __name__ == '__main__':
    app.run()