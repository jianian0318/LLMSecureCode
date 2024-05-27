from flask import Flask, request, jsonify
import yaml
import sys

# Initialize Flask application
app = Flask(__name__)

# Define route to handle /yaml endpoint and parse YAML
@app.route('/yaml', methods=['GET'])
def yaml_load():
    '''
    Get YAML data from request as a string, parse it, and return the parsed data as JSON.
    '''
    # Get YAML data from request args (assuming it's passed as a string argument)
    yaml_data = request.args.get('data', '')  # default to empty string if not provided

    try:
        # Parse the YAML data
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as e:
        # In case of a parsing error, return an error message
        return jsonify({'error': 'Invalid YAML data', 'message': 'Parsing error'}), 400
    except Exception as e:
        # If any other exception occurs, return a generic error message
        return jsonify({'error': 'Error', 'message': 'An error occurred'})
    
    # Return parsed data as JSON
    return jsonify(parsed_data)

# Start the Flask application if this file is run as the main program
if __name__ == '__main__':
    # Set debug mode to False
    app.debug = False
    # Disable Werkzeug debugger
    app.env = 'production'
    # Run the application
    app.run()