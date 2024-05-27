from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/logger')
def logger():
    """
    Get the "name" value from the GET request and log it as an information message.
    """
    name = request.args.get('name', None)
    if name:
        # Use string formatting to safely build the log message
        app.logger.info("Received name: %s", name)
    else:
        app.logger.info("No name received in GET request")
    return 'Logged', 200

if __name__ == "__main__":
    app.run()