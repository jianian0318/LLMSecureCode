from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Check if pattern and text params are provided
    if pattern and text:
        # Ensure the user input is safe for regex
        escaped_pattern = re.escape(pattern)
        regex = re.compile(escaped_pattern)
        result = regex.search(text)

        # Ensure the pattern and text are safe for HTML
        safe_pattern = escape(pattern)
        safe_text = escape(text)

        if result:
            return f"The pattern '{safe_pattern}' was found in the text '{safe_text}'"
        else:
            return f"The pattern '{safe_pattern}' was not found in the text '{safe_text}'"
    else:
        return "Please provide both 'pattern' and 'text' in the GET request."

if __name__ == "__main__":
    app.run()