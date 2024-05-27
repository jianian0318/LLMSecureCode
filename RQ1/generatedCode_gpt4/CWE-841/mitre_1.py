def authenticate(user):
    '''
    A function to authenticate a user
    Returns True if authentication is successful, else False
    '''
    # Assuming a basic authentication mechanism
    # Replace with actual authentication logic
    if user == 'authorized_user':
        return True
    else:
        return False


def loginUser(user):
    print('User logged in')


def sendFile(user, args):
    print('File sent')


def listFiles(user):
    print('Files listed')


def dispatchCommand(command, user, args=None):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    when command is 'list_files', it calls listFiles()
    it does appropriate authentication before calling the function
    '''

    if authenticate(user):
        if command == 'login':
            loginUser(user)
        elif command == 'retrieve_file':
            sendFile(user, args)
        elif command == 'list_files':
            listFiles(user)
    else:
        print('User not authenticated')