import os

def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    # Increase the privilege
    raisePrivileges()

    try:
        # Create the directory
        os.mkdir(f'/home/{username}')
    except FileExistsError:
        print(f"Directory '/home/{username}' already exists")

    # Lower the privilege
    lowerPrivileges()