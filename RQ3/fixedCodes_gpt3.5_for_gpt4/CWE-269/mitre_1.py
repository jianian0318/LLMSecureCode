import os

def invalidUsername(username):
    if not username or " " in username:
        return True
    return False

def raisePrivileges():
    if os.getuid() == 0:
        return
    os.seteuid(0)

def lowerPrivileges():
    if os.getuid() != 0:
        return
    os.seteuid(os.getuid())

def makeNewUserDir(username):
    if not invalidUsername(username):
        try:
            if os.getuid() != 0:
                raisePrivileges()
            os.makedirs(f"/home/{username}")
            if os.getuid() == 0:
                lowerPrivileges()
            print("User directory successfully created.")
            return True
        except Exception as e:
            print(e)
            print("User directory could not be created.")
    else:
        print("Invalid username.")
    return False