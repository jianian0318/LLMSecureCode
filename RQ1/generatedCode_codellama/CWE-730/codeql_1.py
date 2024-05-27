from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    matches = re.findall(pattern, text)
    return f"Matches: {matches}"

if __name__ == "__main__":
    app.run()
