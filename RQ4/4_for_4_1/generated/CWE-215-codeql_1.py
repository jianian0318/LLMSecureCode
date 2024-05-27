from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

if __name__ == '__main__':
    # Ensure debug mode is not enabled when deploying
    app.run(debug=False)