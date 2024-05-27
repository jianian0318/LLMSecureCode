import hashlib
import binascii
import os

def get_password_hash(password: str, salt: str=None):
    '''
    Return a hash of the password and salt using PBKDF2_HMAC.
    '''
    if not salt:
        # Generate a random salt
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        
    # Hash the password using PBKDF2_HMAC
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    # Store the salt with the password
    return (salt + pwdhash).decode('ascii')
