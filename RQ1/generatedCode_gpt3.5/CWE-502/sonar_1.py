from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    if request.method == 'POST':
        data = request.get_data()
        parsed_data = yaml.safe_load(data)
        return parsed_data