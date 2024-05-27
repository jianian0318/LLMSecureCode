from flask import Flask, request
import yaml
import html

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    data = request.get_data(as_text=True)
    yaml_data = yaml.safe_load(data)
    return html.escape(str(yaml_data))