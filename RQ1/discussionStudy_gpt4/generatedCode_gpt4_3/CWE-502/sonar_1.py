from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    data = request.data
    try:
        parsed_yaml = yaml.safe_load(data)
        return jsonify(parsed_yaml)
    except yaml.YAMLError as error:
        return jsonify({'error': str(error)})

if __name__ == '__main__':
    app.run()