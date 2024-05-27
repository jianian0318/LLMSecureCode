from hashlib import pbkdf2_hmac


def getHash(password):
    '''
    create a hash of the password with a salt.
    '''
    salt = b'salt'
    iterations = 100000
    key_length = 64
    hash_algorithm = 'sha256'

    return pbkdf2_hmac(hash_algorithm, password, salt, iterations, key_length)