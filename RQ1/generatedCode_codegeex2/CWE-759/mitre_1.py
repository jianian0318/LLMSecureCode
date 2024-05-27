import hashlib

def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()

    # Update the database with username and hashed password
    updateUserLogin(userName, hashed_password)

def updateUserLogin(userName, hashed_password):
    '''
    Update the database with username and hashed password
    '''
    # Implement the updateUserLogin() method to update the database with username and hashed password
    pass
