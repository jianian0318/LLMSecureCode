from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    escaped_pattern = re.escape(pattern)
    regex = re.compile(escaped_pattern)
    result = regex.search(text)
    return str(result)

if __name__ == "__main__":
    app.run()