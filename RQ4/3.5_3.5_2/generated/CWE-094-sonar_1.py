from flask import Flask, request

app = Flask(__name__)

@app.route('/get_module_version')
def get_module_version():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    version = request.args.get('version')

    if version:
        return "Version parameter is missing in the request"

if __name__ == '__main__':
    app.run()