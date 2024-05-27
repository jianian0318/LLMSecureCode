import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Create a new hashlib object
    m = hashlib.md5()

    # Update the hash object with the password and salt
    m.update((password + salt).encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return m.hexdigest()