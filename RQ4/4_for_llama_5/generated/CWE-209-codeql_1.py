from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    # Simulate some computation which could raise an exception
    # Better to handle exceptions here or use more specific exceptions
    return "Some Result"

@app.route('/fixed')
def server_fixed():
    try:
        result = do_computation()
        return Response(result, status=200)
    except Exception:
        # Don't leak exception info to the user
        # Log the exception server-side instead if needed
        return Response("An error occurred. Please try again later.", status=500)

if __name__ == '__main__':
    # Never run production server with Debug True
    # Replace "Your_specific_IP" with the specific IP address
    app.run(host="Your_specific_IP", port=8080, debug=False)