def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    When command is 'list_files', it calls listFiles()
    It does appropriate authentication before calling the function.
    '''

    if command == 'login':
        loginUser(user, args)
    elif command == 'retrieve_file':
        sendFile(user, args)
    elif command == 'list_files':
        listFiles(user, args)

def loginUser(user, args):
    # TODO: Implement loginUser function
    pass

def sendFile(user, args):
    # TODO: Implement sendFile function
    pass

def listFiles(user, args):
    # TODO: Implement listFiles function
    pass