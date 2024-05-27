def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    if command == 'login':
        loginUser(user, args)
    elif command == 'retrieve_file':
        sendFile(user, args)
    elif command == 'list_files':
        listFiles(user)
    else:
        print("Invalid command")

def loginUser(user, args):
    # Authenticate the user and call login function
    pass

def sendFile(user, args):
    # Authenticate the user and call sendFile function
    pass

def listFiles(user):
    # Authenticate the user and call listFiles function
    pass
