import os
from flask import Response, request, Flask
import html

app = Flask(__name__)


@app.route('/reply')
def listFiles():
    '''
    Retrieve "username" from the request's parameters
    Change current directory to /home/{username}
    List all files then return the list as a response.
    '''
    username = request.args.get('username')
    
    # Escape username input to avoid any potential code injection.
    username = html.escape(username)
    
    if username is None:
        return Response("Username not provided", status=400)

    try:
        os.chdir(f'/home/{username}')
        files = os.listdir()
        return Response(files)
    except FileNotFoundError:
        return Response(f"User {username} not found", status=404)
    except Exception as e:
        return Response(str(e), status=500)