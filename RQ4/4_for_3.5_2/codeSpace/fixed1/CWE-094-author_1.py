from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Assume this is an educational tool just to display back the submitted code.
    Instead of executing it, we'll simply return it safely to the user.
    '''
    # Get the user input from the request
    user_code = request.form.get("code")

    # For demonstration, just return the code safely to the user
    # This approach avoids executing potentially harmful code
    if user_code:
        return f"Received code: {user_code}"
    else:
        return "No code received!"

if __name__ == "__main__":
    # Disable debug mode for production safety
    app.run(debug=False)