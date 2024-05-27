from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    raise Exception("An error occurred while processing the request.")

@app.route('/safe')
def server_safe():
    try:
        do_computation()
    except Exception:
        return Response("An error occurred while processing the request.", status=500)

if __name__ == '__main__':
    app.run(debug=True)