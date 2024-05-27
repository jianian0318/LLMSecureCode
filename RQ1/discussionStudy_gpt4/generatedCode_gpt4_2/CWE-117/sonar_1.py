from flask import request, current_app, Flask
import logging

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input_data = request.args.get("input")
    app.logger.error(f"Logging error: {input_data}")
    return 'Logged', 200

if __name__ == '__main__':
    app.run(debug=True)