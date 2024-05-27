from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("secureLogger")

app = Flask(__name__)

@app.route('/logger')
def logger_route():
    '''
    Get the "name" value from the GET request and safely log it as an information message.
    '''
    name = request.args.get('name', '')  # 'name' is the key we want to get, '' is the default value if 'name' is not found
    
    # Sanitize the input using a function
    def sanitize(user_input):
        # Replace newline and carriage return characters
        return user_input.replace('\n', '_').replace('\r', '_')

    sanitized_name = sanitize(name)
    logger.info('Received name: %s', sanitized_name)  # Use '%s' placeholder and pass the user input as an argument
    
    return 'Logged the name', 200  # return HTTP 200 OK response to the client

# You can start the server using this command
if __name__ == '__main__':
    app.run(debug=False)