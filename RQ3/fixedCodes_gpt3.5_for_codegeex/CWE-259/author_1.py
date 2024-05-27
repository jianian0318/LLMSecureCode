def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    admin_password = "admin123" # Store the admin password securely, such as in a database or configuration file.
    
    if password == admin_password:
        return True
    else:
        return False