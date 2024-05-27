from flask import Flask, request, escape
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it safely, and return it.
    Handling user input securely to avoid CWE-79 and others.
    '''
    try:
        # Securely load YAML data from request
        yaml_data = yaml.safe_load(request.data)

        # If needed, properly encode or escape the output to secure against XSS
        return escape(str(yaml_data))

    except Exception:
        # Return a generic error message instead of a detailed exception to avoid CWE-22
        return "An error occurred while processing your request."

if __name__ == '__main__':
    # Production applications should not run with debug=True
    app.run(debug=False)