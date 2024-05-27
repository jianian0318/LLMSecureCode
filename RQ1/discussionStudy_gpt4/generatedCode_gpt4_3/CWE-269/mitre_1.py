import os


def invalidUsername(username):
    # Assuming invalidUsername function checks if the username is invalid.
    # Implement logic as per requirement.
    if not username:
        return True
    return False


def raisePrivileges():
    # Assuming this function raises program privileges. Implement as required.
    pass


def lowerPrivileges():
    # Assuming this function lowers program privileges. Implement as required.
    pass


def makeNewUserDir(username):
    if invalidUsername(username):
        print(f"Invalid username: {username}")
        return False

    raisePrivileges()
    
    try:
        os.makedirs(f"/home/{username}")
        result = True
    except OSError:
        print(f"Creation of the directory /home/{username} failed")
        result = False
    finally:
        lowerPrivileges()

    return result