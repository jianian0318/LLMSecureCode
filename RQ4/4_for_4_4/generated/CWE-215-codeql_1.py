from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

# main driver function
if __name__ == '__main__':
    # run the application
    app.run()