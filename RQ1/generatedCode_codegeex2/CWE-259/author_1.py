def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    if password == "admin123": # This is a placeholder, in a real application, you would use a secure method to store and verify passwords.
        return True
    else:
        return False