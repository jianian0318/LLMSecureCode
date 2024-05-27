import os


def invalidUsername(username):
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
    return not all(char in valid_chars for char in username)


def raisePrivileges():
    os.setuid(0)  # Set user id to root


def lowerPrivileges():
    os.setuid(1000)  # Set user id back to normal user


def makeNewUserDir(username):
    if invalidUsername(username):
        return False

    raisePrivileges()

    try:
        os.makedirs(f"/home/{username}")
    except Exception as e:
        print(f"Could not create directory: {e}")
        lowerPrivileges()
        return False

    lowerPrivileges()
    return True