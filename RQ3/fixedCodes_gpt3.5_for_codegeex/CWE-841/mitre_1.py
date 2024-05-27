def dispatchCommand(command, user, args):
    if command == 'login':
        loginUser(user, args)
    elif command == 'retrieve_file':
        if isAuthenticated(user):
            sendFile(user, args)
        else:
            print("Authentication failed")
    elif command == 'list_files':
        if isAuthenticated(user):
            listFiles(user)
        else:
            print("Authentication failed")
    else:
        print("Invalid command")

def loginUser(user, args):
    # Authenticate the user and call login function
    pass

def sendFile(user, args):
    # Send the file
    pass

def listFiles(user):
    # List the files
    pass

def isAuthenticated(user):
    # Check if the user is authenticated
    return True