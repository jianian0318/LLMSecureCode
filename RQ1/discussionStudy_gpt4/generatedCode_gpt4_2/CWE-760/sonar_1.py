import os
from hashlib import pbkdf2_hmac

def getHash(password):
    '''
    create a hash of the password with a salt.
    '''
    salt = os.urandom(32)
    key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt, key