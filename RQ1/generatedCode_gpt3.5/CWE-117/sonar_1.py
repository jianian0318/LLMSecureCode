from flask import request, current_app, Flask

app = Flask(__name__)


@app.route('/log', methods=['GET'])
def log():
    input_data = request.args.get('input')
    current_app.logger.error(input_data)

    return 'Logged the input data as error.'