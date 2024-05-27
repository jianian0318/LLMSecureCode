from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    input = request.args.get('input')
    current_app.logger.error(input)
    return 'Logging successful'

if __name__ == '__main__':
    app.run()