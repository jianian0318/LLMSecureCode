import getpass

def checkAdminPassword(admin_hashed):
    '''
    Check if the given password hash matches with the admin user password hash.
    '''
    password = getpass.getpass('Enter your password: ')
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    
    if password_hashed == admin_hashed:
        return True
    else:
        return False
#In your main program define below line with your real hashed password 
#admin_hashed = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8" # this is hashed password for "password" using sha256
#checkAdminPassword(admin_hashed)