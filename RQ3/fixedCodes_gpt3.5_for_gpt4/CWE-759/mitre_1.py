import hashlib
import os

def storePassword(userName, password):
    salt = os.urandom(32)
    # generating a cryptographic hash of the password with salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()
    updateUserLogin(userName, hashed_password, salt)

def updateUserLogin(userName, hashed_password, salt):
    print(f'Updated the database with the username: {userName}, hashed password: {hashed_password} and salt: {salt}')