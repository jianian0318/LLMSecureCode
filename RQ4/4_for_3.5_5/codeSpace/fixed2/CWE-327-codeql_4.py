import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password combined with a salt using a stronger cryptographic hash function.
    '''
    # Concatenate the password and salt
    password_salt = password + salt
    
    # Generate the hash using SHA512 algorithm, preferably use SHA-3 if available
    hash_object = hashlib.sha3_512(password_salt.encode())
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    # Return the hash
    return password_hash