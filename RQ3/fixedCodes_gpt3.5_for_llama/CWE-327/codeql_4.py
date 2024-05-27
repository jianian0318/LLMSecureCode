import hashlib
import os

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Encode the password and salt as bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')

    # Generate a random salt
    random_salt = os.urandom(16)
    
    # Create a new SHA-256 hash object
    hash_object = hashlib.pbkdf2_hmac('sha256', password_bytes, random_salt, 100000)

    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hex()

    return password_hash