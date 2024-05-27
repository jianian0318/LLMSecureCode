import hashlib

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Concatenate password and salt.
    salted_password = password + salt
    # Hash the salted password using SHA256.
    hashed_password = hashlib.sha256(salted_password.encode())
    # Return the hexadecimal representation of the hashed password.
    return hashed_password.hexdigest()