from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    version = request.args.get('version')
    exec(f"import urllib{version}")
    return f"Imported urllib{version}"

if __name__ == '__main__':
    app.run()
