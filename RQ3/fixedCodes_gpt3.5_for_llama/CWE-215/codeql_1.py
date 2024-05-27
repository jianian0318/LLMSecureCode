from flask import Flask, abort

app = Flask(__name__)

@app.route('/crash')
def main():
    abort(500)

if __name__ == '__main__':
    app.run(debug=True)