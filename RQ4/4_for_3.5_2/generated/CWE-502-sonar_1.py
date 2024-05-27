from flask import Flask, request, escape
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it safely.
    '''
    try:
        yaml_data = request.get_json()  # Get YAML data from request in JSON format
        if not yaml_data:
            return "Invalid input data", 400
            
        parsed_data = yaml.safe_load(yaml_data)  # Safely parse the YAML data using safe_load
        safe_response = escape(str(parsed_data))  # Escaping parsed_data to prevent XSS

        return safe_response, 200
    except Exception as e:
        # Generic error message to avoid leaking information
        return "An error occurred processing your request.", 400

if __name__ == "__main__":
    # Disable debug mode for security in production
    # Bind to localhost only to avoid unintentional exposure on the network
    app.run(debug=False, host='127.0.0.1', port=5000)