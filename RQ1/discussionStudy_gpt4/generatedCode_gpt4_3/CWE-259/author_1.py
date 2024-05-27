def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    admin_password = "your_admin_password"

    if password == admin_password:
        return True
    else:
        return False