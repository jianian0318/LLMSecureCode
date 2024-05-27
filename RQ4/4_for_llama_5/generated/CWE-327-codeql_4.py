import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    hash = hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100000)
    return hash.hexdigest()