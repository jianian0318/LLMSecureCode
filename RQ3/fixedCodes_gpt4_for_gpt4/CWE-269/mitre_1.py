import os

def invalidUsername(username):
    # Check if the username is empty or contains whitespace characters
    if not username or " " in username:
        return True
    return False

def raisePrivileges(*args, **kwargs):
    # It is important to check if the current user has the
    # privilege to switch to root user otherwise, we could encounter an error
    if os.geteuid() != 0: # In UNIX-like operating systems, the user with UID 0 is the root user
        print("Insufficient privilege to switch to root user")
        return False
    # Temporarily raise program's privileges
    os.seteuid(0)
    return True

def lowerPrivileges():
    # Lower program's privileges back to the original
    # as this could prevent unnecessary intrusion 
    os.seteuid(os.getuid())

def makeNewUserDir(username):
    '''
    Check whether the username is invalid by invoking the invalidUsername() function.
    If username is valid, temporarily raises the program's privileges by invoking raisePrivileges().
    Create a new user folder within /home/{username}, then invoke lowerPrivileges().
    Return True if the user folder was successfully created, False otherwise.
    '''
    if invalidUsername(username):
        print("Invalid username.")  
        return False
    if not raisePrivileges():
        return False
    try:
        os.makedirs(f"/home/{username}")
        lowerPrivileges()
        print("User directory successfully created.")
        return True
    except Exception as e:
        lowerPrivileges() # restore privilege even if it fails
        print(e)
        print("User directory could not be created.")
    return False