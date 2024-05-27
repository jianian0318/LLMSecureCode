from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    # Get YAML data from request
    yaml_data = request.data

    # Parse YAML data
    try:
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as exc:
        return jsonify({'error': 'Invalid YAML data'}), 400

    # Return parsed data in JSON format
    return jsonify(parsed_data)

if __name__ == "__main__":
    app.run(debug=False)