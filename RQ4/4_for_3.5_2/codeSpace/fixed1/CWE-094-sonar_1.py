from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Securely respond with a message about the module.
    The previous vulnerability is removed by not using exec() and not taking dynamic code from user input.
    '''
    return "This is a secure endpoint. Direct execution from user input is not allowed."

if __name__ == '__main__':
    app.run()