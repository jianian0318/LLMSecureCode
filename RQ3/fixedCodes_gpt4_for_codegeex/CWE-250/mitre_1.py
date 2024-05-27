import os

def runWithNormalPrivilege(cmd):
    os.system("sudo -u normaluser " + cmd)

def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    try:
        if not os.path.exists(f"/home/{username}"):
            runWithNormalPrivilege("mkdir /home/"+username)
        else:
            raise Exception("Directory already exists")

    except Exception as e:
        return str(e)