from flask import Flask, request
import yaml
import html

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        data = yaml.safe_load(request.data)
        if data is not None:
            return html.escape(str(data))

    except Exception as e:
        return "Error processing YAML data"

if __name__ == '__main__':
    app.run()