def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    When command is 'list_files', it calls listFiles()
    It does appropriate authentication before calling the function.
    '''
    if command == 'login':
        if isAuthenticated(user):
            loginUser(user, args)
        else:
            print("User not authenticated!")
    elif command == 'retrieve_file':
        if isAuthenticated(user) and isUserLoggedIn(user):
            sendFile(user, args)
        else:
            print("User not authenticated or not logged in!")
    elif command == 'list_files':
        if isAuthenticated(user) and isUserLoggedIn(user):
            listFiles(user, args)
        else:
            print("User not authenticated or not logged in!")

def isAuthenticated(user):
    # TODO: Implement user authentication
    pass

def isUserLoggedIn(user):
    # TODO: Implement user login status check
    pass

def loginUser(user, args):
    # TODO: Implement loginUser function
    pass

def sendFile(user, args):
    # TODO: Implement sendFile function
    pass

def listFiles(user, args):
    # TODO: Implement listFiles function
    pass