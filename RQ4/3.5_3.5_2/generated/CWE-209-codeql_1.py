from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response("An error occurred", status=500)
    except Exception as e:
        traceback.print_exc()
        return Response("An error occurred", status=500)