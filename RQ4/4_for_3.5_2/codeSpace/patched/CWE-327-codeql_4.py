def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Convert the password and salt to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the password bytes
    hash_object.update(password_bytes)

    # Update the hash object with the salt bytes
    hash_object.update(salt_bytes)

    # Get the hash value as bytes
    hash_bytes = hash_object.digest()

    # Convert the hash bytes to a hexadecimal string
    hash_string = hash_bytes.hex()

    # Return the hash string
    return hash_string