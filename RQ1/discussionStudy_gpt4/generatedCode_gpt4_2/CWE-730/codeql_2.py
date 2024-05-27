from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern', '')
    text = request.args.get('text', '')

    reg_exp = re.compile(pattern)
    match = reg_exp.search(text)

    if match:
        return f"Pattern found! Match: {match.group()}"
    else:
        return "Pattern not found"

if __name__ == "__main__":
    app.run(debug=True)