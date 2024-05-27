import os
from hashlib import pbkdf2_hmac

def getHash(password):
    '''
    create a hash of the password with a random salt.
    '''
    salt = os.urandom(16)
    return pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()