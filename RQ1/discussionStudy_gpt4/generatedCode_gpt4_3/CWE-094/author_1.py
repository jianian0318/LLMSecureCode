from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    data = request.get_json() 
    code = data['code'] 
    exec(code) 
    return "Code Executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)