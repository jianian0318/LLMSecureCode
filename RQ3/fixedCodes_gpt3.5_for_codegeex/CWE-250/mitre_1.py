import os

def raisePrivileges():
    # Insert logic here to elevate privileges, for example by using sudo
    os.system('sudo echo ""')

def lowerPrivileges():
    # Insert logic here to lower privileges, for example by using sudo
    os.system('sudo echo ""')

def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory, elevate privileges using raisePrivileges(),
    then lower the privileges using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    try:
        raisePrivileges()

        if not os.path.exists(f"/home/{username}"):
            os.makedirs(f"/home/{username}")
        else:
            raise Exception("Directory already exists")

        lowerPrivileges()

    except Exception as e:
        print(str(e))
        return Response(str(e), status=500)