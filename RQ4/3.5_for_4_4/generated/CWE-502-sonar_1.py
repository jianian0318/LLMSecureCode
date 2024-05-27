from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)
app.config['DEBUG'] = False  # Set debug mode to False

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        yaml_data = request.get_data(as_text=True)
        parsed_data = yaml.safe_load(yaml_data)
        return jsonify(parsed_data)  # Return parsed data as JSON response
    except Exception as e:
        error_message = 'An error occurred during parsing of YAML data.'
        return jsonify({'error': error_message}), 500  # Return error message as JSON response

if __name__ == '__main__':
    app.run()  # Remove debug=True option to disable debug mode