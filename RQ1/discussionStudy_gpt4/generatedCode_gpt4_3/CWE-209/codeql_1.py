from flask import Flask, Response
app = Flask(__name__)
import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
    except Exception as e:
        result = str(e)
    return Response(result, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)