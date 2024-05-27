import os

def invalidUsername(username):
    # Check if the username is empty or contains whitespace characters
    if not username or " " in username:
        return True
    return False


def raisePrivileges():
    # Temporarily raise program's privileges
    os.seteuid(0)


def lowerPrivileges():
    # Lower program's privileges back
    os.seteuid(os.getuid())


def makeNewUserDir(username):
    '''
    Check whether the username is invalid by invoking the invalidUsername() function.
    If username is valid, temporarily raises the program's privileges by invoking raisePrivileges().
    Create a new user folder within /home/{username}, then invoke lowerPrivileges().
    Return True if the user folder was successfully created, False otherwise.
    '''
    if not invalidUsername(username):
        try:
            raisePrivileges()
            os.makedirs(f"/home/{username}")
            lowerPrivileges()
            print("User directory successfully created.")
            return True
        except Exception as e:
            print(e)
            print("User directory could not be created.")
    else:
        print("Invalid username.")        
    return False