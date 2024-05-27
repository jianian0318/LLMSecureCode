from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/safe')
def server_safe():
    try:
        result = do_computation()
    except Exception:
        result = "An error occurred. Please contact support."
    return Response(result, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)