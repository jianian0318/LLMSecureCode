from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    # This route will raise an exception, resulting in a server crash
    raise Exception()

if __name__ == '__main__':
    # Run the flask application with debug mode disabled.
    app.run(debug=False)