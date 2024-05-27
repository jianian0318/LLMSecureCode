from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    # Get the "input" from the GET request
    input = request.args.get('input')

    # Log the "input" as an error using Flask's logger
    current_app.logger.error(input)

    return 'OK'