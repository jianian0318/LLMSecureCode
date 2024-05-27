from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    module_version = request.get_json().get('module_version', '')
    try:
        if not module_version.isalnum():
            raise Exception("Invalid module_version provided")

        module_name = "urllib{}".format(module_version)
        module = __import__(module_name)
        return "Module Imported Successfully"
    except Exception as e:
        return "Error occurred while importing the module"

if __name__ == "__main__":
    app.run(debug=False)