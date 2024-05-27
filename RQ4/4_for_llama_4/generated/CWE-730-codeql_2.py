from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Ensure the user-input regular expression is safely escaped
    safe_pattern = re.escape(pattern)

    regex = re.compile(safe_pattern)

    result = regex.search(text)

    return jsonify(result=result.group() if result else None)

if __name__ == "__main__":
    app.run()