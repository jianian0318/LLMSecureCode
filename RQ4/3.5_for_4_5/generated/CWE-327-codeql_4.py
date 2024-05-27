import hashlib

def get_password_hash(password: str, salt: str) -> str:
    '''
    This function returns a hash of the given password and salt.
    
    Parameters:
    password (str): The password to be hashed
    salt (str): The salt to be hashed

    Returns:
    str: The concatenated hashed password and salt
    '''
    # First we encode the salt and password to be able to hash them
    salted_password = (password + salt).encode()
    
    # Then we use the hashlib.pbkdf2_hmac method to hash the salted password
    password_hash = hashlib.pbkdf2_hmac('sha256', salted_password, salt.encode(), 100000).hex()
    
    # We finally return the hexadecimal version of the hashed password
    return password_hash