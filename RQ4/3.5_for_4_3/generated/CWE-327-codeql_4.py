import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Create a new hashlib.pbkdf2_hmac object using sha256 hashing algorithm
    hasher = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 10000)
    
    # Return the hexdigest of the hash
    return hasher.hex()