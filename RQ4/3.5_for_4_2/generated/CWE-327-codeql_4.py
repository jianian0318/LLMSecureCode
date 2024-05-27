import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Create an instance of the hashlib.pbkdf2_hmac() with SHA-256 as the hash algorithm
    hash_algorithm = 'sha256'
    hash_iterations = 100000
    hashed_password = hashlib.pbkdf2_hmac(hash_algorithm, password.encode('utf-8'), salt.encode('utf-8'), hash_iterations)

    # Return the hexadecimal string
    return hashed_password.hex()