admin_password = "admin1234"

def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    
    if password == admin_password:
        return True # Password is valid
    else:
        return False # Password is invalid

# Example of use
print(checkAdminPassword("admin1234")) # This should print: True
print(checkAdminPassword("wrong_password")) # This should print: False