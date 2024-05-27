from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    input_val = request.args.get('input')
    current_app.logger.error(input_val)
    return 'Logged input as error'