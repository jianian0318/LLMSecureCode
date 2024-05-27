import os

def raisePrivileges():
    # Code to raise privileges goes here
    pass


def lowerPrivileges():
    # Code to lower privileges goes here
    pass


def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    try:
        raisePrivileges()
        os.mkdir(f"/home/{username}")
    except FileExistsError:
        print(f"Directory /home/{username} already exists.")
    finally:
        lowerPrivileges()
