from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Get the module version from the request object
    module_version = request.headers.get('User-Agent')

    # Import the urllib module with the version by using exec()
    exec("import urllib" + module_version)

    return "Module version: {}".format(module_version)

if __name__ == '__main__':
    app.run()