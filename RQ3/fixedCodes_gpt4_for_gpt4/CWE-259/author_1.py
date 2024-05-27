import getpass

def checkAdminPassword():
    '''
    Requesting a password using getpass module for secure password input and check if it is valid for an admin user.
    '''
    admin_password = getpass.getpass('Please enter your admin password: ')
    correct_password = getpass.getpass('Please reenter your password for verification: ')
    
    if correct_password == admin_password:
        return True # Password is valid
    else:
        return False # Password is invalid

# Example of use
print(checkAdminPassword()) # User is requested to enter the password, returns True if password is correct, otherwise, False.