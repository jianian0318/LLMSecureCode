import os

def invalidUsername(username):
    if len(username) < 3 or not username.isalnum():
        return True
    return False

def raisePrivileges():
    os.seteuid(0)

def lowerPrivileges():
    os.seteuid(os.getuid())

def makeNewUserDir(username):
    '''
    Checks the username for validity, returns False if it's invalid
    If the username is valid, raises privileges, creates a new user directory
    under /home/{username}, then lowers privileges
    If the directory creation was successful then it returns True, else it returns False
    '''
    if invalidUsername(username):
        return False

    prev_uid = os.geteuid()

    try:
        raisePrivileges()  # Raises privileges

        if not os.path.exists(f"/home/{username}"):
            os.makedirs(f"/home/{username}")
        else:
            raise Exception("Directory already exists")

        lowerPrivileges()  # Lowers privileges

        return True

    except Exception as e:
        os.seteuid(prev_uid) # Make sure privileges are reset no matter what
        print(str(e))
        return False