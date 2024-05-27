import hashlib


def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()
    updateUserLogin(userName, hashed_password)