from flask import Response, request, Flask
import os
import json

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')
    username = username.replace("..", "")

    if not os.path.exists(f'/home/{username}'):
        return Response("Directory does not exists!",status=400, mimetype='application/json')

    os.chdir(f'/home/{username}')
    files = os.listdir()
    return Response(json.dumps({'files': files}), mimetype='application/json')

if __name__ == '__main__':
    app.run()