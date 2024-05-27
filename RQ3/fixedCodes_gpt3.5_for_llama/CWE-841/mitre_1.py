import sys

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

def loginUser(user, args):
    # authenticate user logic here
    if user == "admin" and args == "password":
        return True
    else:
        return False
    
def authenticateUser(user):
    # authenticate user logic here
    if user == "admin":
        return True
    else:
        return False
    
def sendFile(user, args):
    # send file logic here
    print("Sending file to user:", user)
    
def listFiles(user):
    # list files logic here
    print("Listing files for user:", user)