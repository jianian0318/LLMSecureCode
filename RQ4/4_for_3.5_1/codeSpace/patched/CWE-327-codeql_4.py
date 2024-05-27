def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Combine the password and salt
    password_salt = password + salt

    # Create a new SHA256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the password salt
    hash_object.update(password_salt.encode())

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()

    # Return the hash
    return hash_hex