import hashlib
import os
import binascii

def get_password_hash(password: str):
    '''
    Return a salt and a hash of the password and salt.
    '''
    # Generate a salt
    salt = os.urandom(16)
    
    # Encode the password and salt as bytes
    password_bytes = password.encode('utf-8')
    
    # Use the PBKDF2_HMAC method for hashing
    password_hash = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 100000)

    # Get the hexadecimal representation of the hash
    password_hash = binascii.hexlify(password_hash)

    return salt, password_hash