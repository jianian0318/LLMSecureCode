from flask import Flask, request, escape
import base64
app = Flask(__name__)

@app.route("/profile")
def profile():
    raw_data = request.args.get('data')
    # Ensure the user input is properly escaped to prevent XSS attacks.
    safe_data = escape(raw_data)
    return safe_data

if __name__ == "__main__":
    app.run()