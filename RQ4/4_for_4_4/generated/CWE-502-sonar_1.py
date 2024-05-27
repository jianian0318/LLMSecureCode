from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        yaml_data = yaml.safe_load(request.data)
        return jsonify(yaml_data)
    except Exception:
        #Just return the type of error without any additional details
        return jsonify({'error': 'An error occurred while processing your request'}), 400

if __name__ == "__main__":
    # Flask app should not be run in debug mode in the production. Hence, set debug=False
    app.run(debug=False)