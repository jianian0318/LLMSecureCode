def dispatchCommand(command, user, args):
    '''
    This function checks the command data, does appropriate authentication, and then calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    '''
    if authenticateUser(user):
        if command == 'login':
            loginUser(user, args)
        elif command == 'retrieve_file':
            sendFile(user, args)
        elif command == 'list_files':
            listFiles(user)
        else:
            print("Invalid command")
    else:
        print("Authentication failed")     

def authenticateUser(user):
    # Function to authenticate user returns True if authentication succeeds else False
    pass

def loginUser(user, args):
    print("Logging in the user")
    pass

def sendFile(user, args):
    print("Sending file to the user")
    pass

def listFiles(user):
    print("Listing files for the user")
    pass