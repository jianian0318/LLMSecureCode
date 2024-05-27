import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Concatenate the password and salt
    password_salt = password + salt
    
    # Generate the hash using SHA256 algorithm
    hash_object = hashlib.sha256(password_salt.encode())
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    # Return the hash
    return password_hash