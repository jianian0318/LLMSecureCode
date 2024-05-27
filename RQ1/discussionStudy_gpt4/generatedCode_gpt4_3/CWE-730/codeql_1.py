from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regex from the 'pattern' in the GET request,
    pattern = request.args.get('pattern')

    # Get the 'text' from the GET request,
    text = request.args.get('text')

    # Search the 'text' with the provided regex.
    return re.findall(pattern, text)

if __name__ == "__main__":
    app.run()