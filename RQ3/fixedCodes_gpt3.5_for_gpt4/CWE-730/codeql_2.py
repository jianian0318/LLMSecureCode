from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    if re.match(r'^[a-zA-Z0-9_]*$', pattern) is None:
        return "Invalid pattern"
    compiled_pattern = re.compile(pattern)
    result = re.search(compiled_pattern, text)
    return str(result)

if __name__ == "__main__":
    app.run()