import re
from flask import Flask, request

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Ensure that pattern is a safe string
    safe_pattern = re.escape(pattern)

    compiled_pattern = re.compile(safe_pattern)
    result = re.search(compiled_pattern, text)
    return str(result)


if __name__ == "__main__":
    app.run()