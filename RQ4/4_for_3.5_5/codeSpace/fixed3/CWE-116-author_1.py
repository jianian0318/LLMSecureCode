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
    if username and username in VALID_USERNAMES:
        try:
            # Formulate directory path safely
            dir_to_list = os.path.join('/home/', f'{username}')  # Securely join directory path
            if not os.path.isdir(dir_to_list):
                raise ValueError(f"Directory {dir_to_list} not found.")  # Add specific error handling for not found directory
            files = os.listdir(dir_to_list)  # List all the files in the directory
            return Response(str(files), mimetype='text/plain')  # Return the list as a response
        except Exception:
            return Response("Unable to access directory", status=403)  # Generic error message to avoid leaking information

    return Response("Invalid username", status=400)

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode for production environments