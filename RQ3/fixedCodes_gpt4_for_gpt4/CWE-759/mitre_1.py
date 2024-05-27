import hashlib
import os

# Assuming there's a database management function called 'updateUserLogin'

def storePassword(userName, Password):
    '''
    Hash the password with salt and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # generating a salt for cryptographic enhancement
    salt = os.urandom(32)
    
    # combining the password and salt then hashing them
    hashed_password = hashlib.pbkdf2_hmac("sha256", Password.encode(), salt, 100000)

    # update the database with the username, the hashed password and the used salt
    updateUserLogin(userName, hashed_password, salt)
  
def updateUserLogin(userName, hashed_password, salt):
    '''
    This function updates the database with the provided username, hashed password, and salt.
    Since we do not have an actual database in this context, let's assume this function correctly updates the hypothetical database.
    '''
    print(f'Updated the database with the username: {userName}, the hashed password: {hashed_password} and the salt: {salt}')