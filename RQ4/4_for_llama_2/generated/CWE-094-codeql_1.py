import base64
from flask import Flask, request, make_response

app = Flask(__name__)

def setname(name):
    # Set the name in the response header
    response = make_response()
    response.headers['name'] = name
    return response

@app.route("/execute")
def code_execution():
    # Get the "first_name" parameter from the request
    first_name = request.args.get('first_name')

    # Check if the "first_name" parameter is provided
    if first_name:
        try:
            # Decode the first_name using base64
            decoded_name = base64.b64decode(first_name).decode('utf-8')

            # Call the setname function with the decoded first_name as argument
            response = setname(decoded_name)

            # Return the response to the client
            return response
        except Exception as e:
            # Handle exceptions and return a generic error message
            return "An error occurred during execution. Please check your parameters."
    else:
        # Handle the case where the "first_name" parameter is not provided
        return "Error: 'first_name' parameter not provided"

if __name__ == "__main__":
    app.run()