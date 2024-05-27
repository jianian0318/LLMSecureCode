import os

def raisePrivileges():
    # 在此处添加提升权限的逻辑，例如调用系统命令
    pass

def lowerPrivileges():
    # 在此处添加降低权限的逻辑，例如调用系统命令
    pass

def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    try:
        raisePrivileges()  # 提升权限

        if not os.path.exists(f"/home/{username}"):
            os.makedirs(f"/home/{username}")
        else:
            raise Exception("Directory already exists")

        lowerPrivileges()  # 降低权限

    except Exception as e:
        e.traceback.print_exc()
        return Response(str(e), status=500)
