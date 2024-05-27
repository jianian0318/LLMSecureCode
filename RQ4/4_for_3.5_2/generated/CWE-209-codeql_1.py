from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    # Simulated computation function that may raise an exception
    raise Exception("Secret info")

@app.route('/compute')
def server_compute():
    try:
        result = do_computation()
        return Response(str(result), status=200)
    except Exception:
        # Return a generic error response without leaking sensitive details
        return Response("An error occurred during computation.", status=500)

if __name__ == '__main__':
    app.run()