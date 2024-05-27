from flask import Flask, request, make_response
from compile import compile_source
import execjs

app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    user_input = request.args.get('code')
    
    try:
        compiled_code = compile_source(user_input)
        result = execjs.compile(compiled_code).call("eval", user_input)
        response = make_response(str(result))
    except Exception as e:
        response = make_response(str(e))
        response.status_code = 400

    return response
