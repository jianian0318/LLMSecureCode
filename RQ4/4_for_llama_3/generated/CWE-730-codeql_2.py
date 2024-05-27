from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    pattern = re.escape(pattern)                      # escape user input to prevent ReDoS

    compiled_pattern = re.compile(pattern)
    result = compiled_pattern.search(text)

    return str(result)                                # return as string because Flask can't return Match object

if __name__ == "__main__":
    app.run()