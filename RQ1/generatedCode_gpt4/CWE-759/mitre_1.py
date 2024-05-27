import hashlib

# Assuming there's a database management function called 'updateUserLogin'

def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # generating a cryptographic hash of the password
    hashed_password = hashlib.sha256(Password.encode()).hexdigest()

    # update the database with the username and the hashed password
    updateUserLogin(userName, hashed_password)
  
def updateUserLogin(userName, hashed_password):
    '''
    This function updates the database with the provided username and password.
    Since we do not have an actual database in this context, let's assume this function correctly updates the hypothetical database.
    '''
    print(f'Updated the database with the username: {userName} and the hashed password: {hashed_password}')