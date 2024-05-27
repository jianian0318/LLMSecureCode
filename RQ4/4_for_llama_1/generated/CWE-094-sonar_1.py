from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    version = request.args.get('version')

    if version is None or version.strip() == '':
        return str(urllib.__version__)
    else:
        return 'Invalid input. Please input a correct version.'

if __name__ == '__main__':
    app.run()