from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    input = request.args.get('input')
    current_app.logger.error(input)
    return "Logged the input as an error"

if __name__ == '__main__':
    app.run()