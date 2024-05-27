import sys

def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    When command is 'list_files', it calls listFiles()
    It does appropriate authentication before calling the function.
    '''

    if command == 'login':
        if authenticateUser(user, args):
            loginUser(user, args)
        else:
            print("Authentication failed.")
    elif command == 'retrieve_file':
        if authenticateUser(user, args):
            sendFile(user, args)
        else:
            print("Authentication failed.")
    elif command == 'list_files':
        if authenticateUser(user, args):
            listFiles(user, args)
        else:
            print("Authentication failed.")
    else:
        print("Invalid command.")

def authenticateUser(user, args):
    # TODO: Implement authentication logic
    # Return True or False based on the authentication result
    return True

def loginUser(user, args):
    # TODO: Implement loginUser function
    pass

def sendFile(user, args):
    # TODO: Implement sendFile function
    pass

def listFiles(user, args):
    # TODO: Implement listFiles function
    pass