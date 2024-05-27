import hashlib
import os

def storePassword(userName, Password):
    '''
    Hash the password and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    # Generate a random salt
    salt = os.urandom(32)

    # Hash the password along with salt using SHA-256
    hashed_password = hashlib.pbkdf2_hmac('sha256', Password.encode(), salt, 100000)

    # Store salt with the hashed password
    stored_password = salt + hashed_password

    # Update the database with username and stored password
    updateUserLogin(userName, stored_password)

def updateUserLogin(userName, stored_password):
    '''
    Update the database with username and stored password
    '''
    # Implement the updateUserLogin() method to update the database with username and stored password
    pass