def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''
    if command == 'login':
        if loginUser(user, args):
            print("User logged in successfully")
        else:
            print("Login failed")
    elif command == 'retrieve_file':
        if authenticateUser(user):
            sendFile(user, args)
        else:
            print("Authentication failed")
    elif command == 'list_files':
        if authenticateUser(user):
            listFiles(user)
        else:
            print("Authentication failed")
    else:
        print("Invalid command")
