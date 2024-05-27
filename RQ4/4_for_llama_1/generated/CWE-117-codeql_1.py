from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.INFO)

# Create a custom logger
logger = logging.getLogger("my_logger")

# Prevent flask's default logger from handling messages
logger.propagate = False

# Configure the logger to use a safer formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Sanitize user input to ensure it's safe to log
def sanitize(input_string):
    # Replace line break characters with a space
    sanitized = input_string.replace('\n', ' ').replace('\r', ' ')
    # Log what is essentially now one single line
    return sanitized

app = Flask(__name__)

@app.route('/logger')
def logger_route():
    # get 'name' from request args
    name = request.args.get('name', '')

    # Sanitize the user-provided 'name' to prevent log injection
    sanitized_name = sanitize(name)

    # log the sanitized name
    logger.info(f"Name: {sanitized_name}")
    
    return "Logged successfully"

if __name__ == "__main__":
    app.run()