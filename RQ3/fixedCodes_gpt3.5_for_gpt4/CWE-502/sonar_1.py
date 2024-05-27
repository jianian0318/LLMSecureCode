import yaml
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    try:
        data = request.data
        yaml_data = yaml.safe_load(data)
        return json.dumps(yaml_data)
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run()