from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

if __name__ == '__main__':
    # Set debug to False for production environment to avoid potential security risks
    app.run(debug=False)