import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    salted_password = password + salt
    
    return hashlib.pbkdf2_hmac('sha256', salted_password.encode(), salt.encode(), 100000).hex()