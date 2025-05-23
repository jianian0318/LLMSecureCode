from hashlib import pbkdf2_hmac
import os


def getHash(password):
    '''
    create a hash of the password with a salt.
    '''
    salt = os.urandom(16)
    key = pbkdf2_hmac(
        'sha256',  # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,  # Provide the salt
        100000  # It is recommended to use at least 100,000 iterations of SHA-256
    )
    return salt + key  # Combine the salt and the key
