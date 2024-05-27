import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Encode the password and salt as bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the password and salt bytes
    hash_object.update(password_bytes + salt_bytes)

    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()

    return password_hash
