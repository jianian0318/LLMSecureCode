import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    salted_password = salt + password
    password_hash = hashlib.sha256(salted_password.encode()).hexdigest()
    return password_hash