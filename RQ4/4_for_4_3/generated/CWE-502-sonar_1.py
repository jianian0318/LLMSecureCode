from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    # Read the raw text data from the request
    yaml_data = request.data

    try:
        # Parse the YAML data using yaml.safe_load to prevent code execution
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError:
        # Do not return the exception details as it might leak information
        # Return a generic error message instead
        return jsonify({'error': 'Invalid YAML data'}), 400

    # Return the parsed data as JSON
    return jsonify(parsed_data)

if __name__ == '__main__':
    # Do not run the Flask app in debug mode in a production environment
    app.run(debug=False)