def dispatchCommand(command, user, args):
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

def authenticateUser(user):
    # Perform authentication logic here
    if user == 'admin':
        return True
    else:
        return False

def loginUser(user, args):
    # Perform login logic here
    if user == 'admin' and args == 'password':
        return True
    else:
        return False

def sendFile(user, args):
    # Perform sendFile logic here
    print(f"Sending file {args} to {user}")

def listFiles(user):
    # Perform listFiles logic here
    print(f"Listing files for {user}")

dispatchCommand('login', 'admin', 'password')
dispatchCommand('retrieve_file', 'admin', 'file.txt')
dispatchCommand('list_files', 'admin', '')
dispatchCommand('invalid_command', 'admin', '')