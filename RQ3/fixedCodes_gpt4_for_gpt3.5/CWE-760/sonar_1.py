import os
from hashlib import pbkdf2_hmac


def getHash(password):
    '''
    create a hash of the password with a secure, randomly-generated salt.
    '''
    salt = os.urandom(16)  # Generates a secure, random 16-byte salt
    iterations = 100000
    key_length = 64
    hash_algorithm = 'sha256'

    return pbkdf2_hmac(hash_algorithm, password.encode('utf-8'), salt, iterations, key_length), salt

# Note: In the fixed code, the salt is now generated using `os.urandom(16)` to create a secure, random 16-byte salt. The password is also encoded to bytes before being used in the hashing function, to ensure compatibility with the `pbkdf2_hmac` function. The modified function also returns the generated salt, as storing the salt is necessary for future password verifications.