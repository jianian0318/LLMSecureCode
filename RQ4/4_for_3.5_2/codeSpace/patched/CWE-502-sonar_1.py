from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        yaml_data = request.get_json() # Get YAML data from request in JSON format
        parsed_data = yaml.load(yaml_data, Loader=yaml.Loader) # Parse the YAML data
        return parsed_data, 200
    except Exception as e:
        return str(e), 400