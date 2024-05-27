import hashlib

def get_password_hash(password: str, salt: str) -> str:
    '''
    Return a hash of the password and salt.
    '''
    # create a new sha256 hash object
    sha256_hash = hashlib.sha256()

    # add password and salt
    sha256_hash.update(password.encode('utf-8'))
    sha256_hash.update(salt.encode('utf-8'))

    # return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()