from flask import Flask, Response
import traceback

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return Response(str(result), status=200)
    except Exception as e:
        traceback.print_exc()
        return Response(str(e), status=500)

if __name__ == '__main__':
    app.run()