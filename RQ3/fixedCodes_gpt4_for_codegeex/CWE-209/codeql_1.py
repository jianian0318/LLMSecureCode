from flask import Flask, Response
import traceback

app = Flask(__name__)


def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Perform computation within a try-except block,
    Return a Response that contains the result of the computation.
    '''
    try:
        result = do_computation()
        return Response(str(result))
    except Exception as e:
        # do not pass exception to Response - provides sensitive data
        print("Exception Occurred, Error handled") # for logging purposes
        return Response("An error has occurred", status=500)