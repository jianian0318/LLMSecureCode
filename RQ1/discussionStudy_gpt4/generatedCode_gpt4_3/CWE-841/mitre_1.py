def authenticate(user):
    '''
    This function is just a placeholder for the actual authentication logic. 
    '''
    print(f"User {user} authenticated")
    return True

def loginUser(user):
    '''
    This function is a placeholder for actual login logic
    '''
    print(f"User {user} logged in.")
  
def sendFile(user, args):
    '''
    This function is a placeholder to send file.
    '''
    print(f"File {args} sent to user {user}.")

def listFiles(user):
    '''
    This function is placeholder to list all files of user.
    '''
    print(f"Listed files of user {user}.")

def dispatchCommand(command, user, args=None):
    if authenticate(user):
        if command == 'login':
            loginUser(user)
        elif command == 'retrieve_file':
            if args is not None:
                sendFile(user, args)
            else:
                print("Error: No file specified.")
        elif command == 'list_files':
            listFiles(user)
        else:
            print("Error: Invalid command.")