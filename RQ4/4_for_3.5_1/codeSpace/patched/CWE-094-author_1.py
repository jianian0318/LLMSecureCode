from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    code = request.form.get('code')
    try:
        result = exec(code)
        return str(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()