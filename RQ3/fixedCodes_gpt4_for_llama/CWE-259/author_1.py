def checkAdminPassword(password, admin_password):
    '''
    Check if the password is valid for an admin user.
    '''
    special_characters = '!@#$%^&*()-+?_=,<>/'
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in special_characters for char in password):
        return False
    if password != admin_password:
        return False
    return True