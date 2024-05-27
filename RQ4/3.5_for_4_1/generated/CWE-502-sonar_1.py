from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    # This assumes that the yaml data is sent through the request body.
    yaml_data = request.data
    
    # Parse the yaml data with safe_load, which avoids loading arbitrary objects.
    try:
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError:
        # Handle YAML parse errors (e.g., improper YAML syntax).
        return jsonify({'error': 'Invalid YAML data'}), 400

    # Return parsed data as JSON.
    return jsonify(parsed_data)

if __name__ == '__main__':
    app.run()