import os

def raisePrivileges():
    os.setuid(0)

def lowerPrivileges(original_uid):
    os.setuid(original_uid)

def makeNewUserDir(username):
    try:
        # Save original user ID
        original_uid = os.getuid()

        # Temporarily raise privileges
        raisePrivileges()

        # Create user directory
        os.mkdir('/home/' + username)
    
    except FileExistsError:
        print(f'Directory /home/{username} already exists.')
    
    finally:
        # Always lower privileges, even if an error occurred
        lowerPrivileges(original_uid)