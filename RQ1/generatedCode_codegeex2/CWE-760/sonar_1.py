from hashlib import pbkdf2_hmac

def getHash(password):
    '''
    create a hash of the password with a salt.
    '''
    return pbkdf2_hmac('sha256', password.encode(), b'salt', 100000).hex()