import hashlib


def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    password = password.encode()  # Convert the password to bytes
    salt = salt.encode()  # Convert the salt to bytes

    hashed_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    # pbkdf2_hmac requires the name of the hash function ('sha256' here), 
    # the password to hash, a salt, and the number of iterations

    return hashed_password.hex()  # Return the hexadecimal representation of the hash