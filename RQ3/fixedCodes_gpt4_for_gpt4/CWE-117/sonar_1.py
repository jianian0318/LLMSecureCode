from flask import request, current_app, Flask
import logging
from html import escape

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)

@app.route('/log')
def log():
    input_val = request.args.get('input', None)
    if input_val:
        sanitized_input = escape(input_val)
        current_app.logger.error(f'Error Message: {sanitized_input}')
        return "Logged Successfully", 200
    else:
        return "No input data provided", 400

if __name__ == "__main__":
    app.run(debug=True)