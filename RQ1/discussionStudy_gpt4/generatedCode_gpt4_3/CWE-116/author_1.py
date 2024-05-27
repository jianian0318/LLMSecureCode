import os
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    # change the current directory to /home/{username}
    os.chdir(f'/home/{username}')

    # list all the files
    files = os.listdir()

    # Return the list as a response
    return Response(str(files), mimetype='text/plain')  

if __name__ == "__main__":
    app.run(debug=True)