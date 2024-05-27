from flask import request, current_app, Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)

@app.route('/log')
def log():
    input_val = request.args.get('input', None) 
    if input_val:
        current_app.logger.error(f'Error Message: {input_val}')
        return "Logged Successfully", 200
    else:
        return "No input data provided", 400

if __name__ == "__main__":
    app.run(debug=True)