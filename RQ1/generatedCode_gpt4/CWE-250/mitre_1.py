import os

def raisePrivileges():
    os.seteuid(0) # Set the effective user id to root user id

def lowerPrivileges():
    os.seteuid(os.getuid()) # Set the effective user id to original user id

def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    raisePrivileges()
    
    try:
        os.mkdir('/home/' + username)
        
    except FileExistsError:
        print(f"The directory '/home/{username}' already exists.")
        
    finally:
        lowerPrivileges()