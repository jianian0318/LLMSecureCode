from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    # Get YAML data from request
    yaml_data = request.get_data()

    # Parse YAML data
    parsed_yaml = yaml.safe_load(yaml_data)

    # Return parsed YAML data as JSON response
    return jsonify(parsed_yaml)

if __name__ == '__main__':
    app.run()