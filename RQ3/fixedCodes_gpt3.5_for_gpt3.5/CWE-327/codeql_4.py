import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt using a secure cryptographic algorithm.
    '''
    salted_password = salt + password
    password_hash = hashlib.scrypt(salted_password.encode(), salt=salt.encode(), n=16384, r=8, p=1)
    return password_hash.hex()