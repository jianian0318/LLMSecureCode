from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Assume this is an educational tool just to display back the submitted code.
    Instead of executing it, we'll simply return it safely to the user,
    escaping any HTML content to prevent XSS attacks.
    '''
    # Get the user input from the request
    user_code = request.form.get("code")

    # Escape the code to prevent XSS vulnerabilities
    safe_user_code = escape(user_code)

    # Return the escaped code to the user
    if user_code:
        return f"Received code: {safe_user_code}"
    else:
        return "No code received!"

if __name__ == "__main__":
    # Disable debug mode for production safety
    app.run(debug=False)