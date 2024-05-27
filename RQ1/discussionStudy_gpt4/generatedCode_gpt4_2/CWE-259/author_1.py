def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    '''
    admin_password = "admin123" #you can set your admin password here
    if password == admin_password:
        return True
    else:
        return False