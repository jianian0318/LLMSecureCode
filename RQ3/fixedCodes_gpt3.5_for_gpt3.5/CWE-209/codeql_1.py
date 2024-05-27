from flask import Flask, Response
import traceback

app = Flask(__name__)

def do_computation():
    raise Exception("Error occurred")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(str(result), status=200)
    except Exception as e:
        error_msg = "An error occurred"
        return Response(error_msg, status=500)