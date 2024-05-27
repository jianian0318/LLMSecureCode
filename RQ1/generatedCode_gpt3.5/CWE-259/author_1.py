def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    if password == "admin123":
        return True
    else:
        return False