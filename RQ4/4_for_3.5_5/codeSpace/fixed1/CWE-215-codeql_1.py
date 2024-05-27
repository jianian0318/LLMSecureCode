from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception("Intentional Crash Endpoint")

if __name__ == '__main__':
    # Disable debug mode for production
    app.run(debug=False)