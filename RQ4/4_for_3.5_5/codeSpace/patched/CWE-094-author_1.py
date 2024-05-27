from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    code = request.get_data(as_text=True)
    locals_dict = {}
    exec(code, globals(), locals_dict)
    output = locals_dict.get('__builtins__').get('str')(locals_dict)
    return output
    
if __name__ == "__main__":
    app.run(debug=True)