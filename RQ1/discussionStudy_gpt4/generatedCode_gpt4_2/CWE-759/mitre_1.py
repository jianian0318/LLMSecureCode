import hashlib

# Let's assume we have a function named updateUserLogin() to update the database
def updateUserLogin(userName, password):
    # Connection to the database and updating stats will be in here
    pass

def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()
    updateUserLogin(userName, hashed_password)

# Test
storePassword('testUser', 'testPassword')