from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.errorhandler(Exception)
def handle_exception(e):
    response = {"message": "An error occurred"}
    return jsonify(response), 500

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''

    # Check if request contains data
    if request.data:
        yaml_data = request.data

        try:
            # Use safe_load to parse YAML data
            parsed_yaml = yaml.safe_load(yaml_data)
            return jsonify(parsed_yaml), 200
        except yaml.YAMLError as error:
            response = {"message": "Error parsing YAML"}
            return jsonify(response), 400

    else:
        response = {"message": "No data provided"}
        return jsonify(response), 400

if __name__ == "__main__":
    app.run(debug=False)