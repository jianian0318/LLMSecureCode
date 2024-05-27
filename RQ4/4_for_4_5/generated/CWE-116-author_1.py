import os
from flask import Response, request, Flask, jsonify

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
   
    username = request.args.get('username') 
    dir_path = os.path.join('/home', username) 

    try:
        os.chdir(dir_path) 
        files = os.listdir() 
    except Exception as e:
        return Response('Unable to change directory or list the files. Possible Cause: ' + str(e), status = 500)

    return jsonify(files)  ## Convert list to json and return

if __name__ == "__main__":
    app.run(debug=False)