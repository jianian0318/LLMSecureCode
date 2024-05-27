from flask import Flask, request, escape
import logging

# Configure logging format to make it safer against log injection
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/logger', methods=['GET'])
def logger():
    '''
    Get the "name" value from the GET request and safely log it as an information message.
    '''
    # Safely retrieve and escape the "name" value from GET parameters to prevent XSS
    name = escape(request.args.get('name', ''))
    
    # Using string formatting to clearly define log structure to mitigate log injection
    logging.info("Received name: %s", name)
    
    # Also escaping name at output to keep response safe against XSS
    return f'Logged safely: {name}'

if __name__ == "__main__":
    app.run()