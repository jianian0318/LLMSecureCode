def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''

    def loginUser(user, password):
        # Code for logging in user goes here.
        pass

    def sendFile(user, file):
        # Code for sending files goes here.
        pass

    def listFiles(user):
        # Code for listing files goes here.
        pass

    def authenticate(user):
        # Code for authenticating a user goes here.
        # This function should return a boolean value indicating whether the user is authenticated or not.
        pass

    isAuthenticated = authenticate(user)
    if isAuthenticated:
        if command == 'login':
            loginUser(user, args[0])  # Assuming password is the first argument
        elif command == 'retrieve_file':
            sendFile(user, args[0])  # Assuming filename is the first argument
        elif command == 'list_files':
            listFiles(user)
        else:
            print('Invalid command')
    else:
        print('User not authenticated')