from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        # Get YAML data from request and parse it
        yaml_data = yaml.safe_load(request.data)

        # Return parsed YAML data
        return yaml_data

    except Exception as e:
        # Return error message if there is an exception
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)