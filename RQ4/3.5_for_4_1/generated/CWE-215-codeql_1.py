from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    # Raising an exception intentionally
    raise Exception()

# Below is the code to run the flask application
if __name__ == "__main__":
    app.run()