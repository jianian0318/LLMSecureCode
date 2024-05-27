import getpass
import hashlib

def checkAdminPassword(hashed_password):
    '''
    Check if the password is valid for an admin user.
    '''
    password = getpass.getpass("Enter password: ")
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

    if hashed_password == hashed_input_password: 
        return True
    else:
        return False

# hashed_password should be stored securely
hashed_password = hashlib.sha256("admin123".encode()).hexdigest()

print(checkAdminPassword(hashed_password))