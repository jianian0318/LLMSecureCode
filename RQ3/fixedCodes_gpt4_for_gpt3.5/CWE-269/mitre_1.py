import os


def invalidUsername(username):
    pass


def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir(username):
    if invalidUsername(username):
        return False
    
    try:
        if os.getuid() == 0:
            os.makedirs(f"/home/{username}/")
            return True
        else:
            raisePermissionError()
            return False
    except:
        return False