from flask import Flask, request
import yaml
import json
import html

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    data = request.get_data(as_text=True)  # retrieve data from request
    try:
        parsed_data = yaml.safe_load(html.escape(data))  # parse YAML data
        return json.dumps(parsed_data)  # return parsed data as JSON
    except Exception as e:
        return "An error occurred."

if __name__ == '__main__':
    app.run()