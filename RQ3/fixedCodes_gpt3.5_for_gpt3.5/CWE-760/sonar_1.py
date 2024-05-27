from hashlib import pbkdf2_hmac
import os


def getHash(password):
    '''
    create a hash of the password with a random salt.
    '''
    salt = os.urandom(16)
    iterations = 100000
    key_length = 64
    hash_algorithm = 'sha256'

    return pbkdf2_hmac(hash_algorithm, password.encode(), salt, iterations, key_length)