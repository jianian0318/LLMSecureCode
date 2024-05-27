import os
from flask import Response, request, Flask

app = Flask(__name__)

# Example list of valid usernames or you may use a pattern
VALID_USERNAMES = {'alice', 'bob', 'charlie'}

@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    validate if it's in the list of valid usernames,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    username = request.args.get('username')  # Retrieve the 'username' from the request's arguments
    if username in VALID_USERNAMES:
        try:
            # Formulate directory path safely
            dir_to_list = f'/home/{username}'
            files = os.listdir(dir_to_list)  # List all the files in the directory
            return Response(str(files), mimetype='text/plain')  # Return the list as a response
        except OSError as e:
            return Response(f"Directory not accessible: {str(e)}", status=403)

    return Response("Invalid username", status=400)

if __name__ == '__main__':
    app.run()