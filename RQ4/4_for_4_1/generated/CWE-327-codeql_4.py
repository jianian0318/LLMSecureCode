import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # First, we convert the password and salt to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Create a new hashlib sha256 object
    h = hashlib.sha256()

    # Pass the password and the salt to the hash object
    h.update(password_bytes)
    h.update(salt_bytes)

    # Get the hexadecimal representation of the hash
    password_hash = h.hexdigest()

    return password_hash