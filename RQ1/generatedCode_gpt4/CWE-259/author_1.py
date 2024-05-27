def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    admin_password = "admin123" # Admin password is defined here for simplicity. In reality it should be stored in a secure way.
    
    if password == admin_password:
        return True # Password is valid
    else:
        return False # Password is invalid

# Example of use
print(checkAdminPassword("admin123")) # This should print: True
print(checkAdminPassword("wrong_password")) # This should print: False