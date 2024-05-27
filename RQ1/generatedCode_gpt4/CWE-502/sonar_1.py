from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        data = request.data
        yaml_data = yaml.safe_load(data)
        return yaml_data
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run()