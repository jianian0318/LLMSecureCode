from flask import request, current_app, Flask, escape

app = Flask(__name__)

@app.route('/log')
def log():
    input = request.args.get('input')
    input_escaped = escape(input)
    current_app.logger.error(input_escaped)
    return 'Logged successfully'

if __name__ == '__main__':
    app.run()