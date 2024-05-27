import bcrypt

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # combine password and salt
    password_salt = password + salt
    
    # generate a new bcrypt hash
    bcrypt_hash = bcrypt.hashpw(password_salt.encode(), bcrypt.gensalt()).decode()
    
    return bcrypt_hash