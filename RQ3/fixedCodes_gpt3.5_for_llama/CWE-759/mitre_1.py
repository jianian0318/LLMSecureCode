import hashlib

def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    salt = "somerandomsalt"
    hashedPassword = hashlib.sha256((Password + salt).encode()).hexdigest()
    updateUserLogin(userName, hashedPassword)