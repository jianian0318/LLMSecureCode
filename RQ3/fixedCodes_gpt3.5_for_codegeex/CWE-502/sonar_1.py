from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        yaml_data = request.get_json()
        parsed_data = yaml.safe_load(yaml_data)
        return parsed_data
    except Exception as e:
        return str(e)