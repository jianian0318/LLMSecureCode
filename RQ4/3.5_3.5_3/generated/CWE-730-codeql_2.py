from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = re.escape(request.args.get('pattern')) # Escaping the user input
    text = request.args.get('text')
    result = re.search(pattern, text)
    if result:
        return 'Found'
    else:
        return 'Not found'

if __name__ == '__main__':
    app.run()