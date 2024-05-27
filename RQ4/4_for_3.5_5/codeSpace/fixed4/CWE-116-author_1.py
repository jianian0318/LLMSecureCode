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
            base_dir = '/home/'
            safe_path = os.path.join(base_dir, username)  # Securely join directory path

            # Check if the path exists and starts with the base_dir (avoid path traversal)
            if os.path.exists(safe_path) and os.path.realpath(safe_path).startswith(os.path.realpath(base_dir)):
                files = os.listdir(safe_path)  # List all the files in the directory
                return Response(str(files), mimetype='text/plain')  # Return the list as a response
            else:
                return Response(f"Directory {safe_path} does not exist or access denied.", status=400)
        except Exception as e:
            return Response(f"Error: {str(e)}", status=500)  # Return a server error

    return Response("Invalid username", status=400)  # If none of the valid usernames, return error

if __name__ == '__main__':
    app.run(debug=False)  # Turn off debug mode for production environments