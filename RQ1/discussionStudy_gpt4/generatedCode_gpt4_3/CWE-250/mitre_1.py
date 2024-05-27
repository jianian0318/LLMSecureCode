import os

def raisePrivileges():
    os.seteuid(0)

def lowerPrivileges():
    os.seteuid(os.getuid())

def makeNewUserDir(username):
    path = "/home/" + username
    try:
        raisePrivileges()
        os.mkdir(path, 0o755)
    except FileExistsError:
        print("Directory already exists.")
    finally:
        lowerPrivileges()