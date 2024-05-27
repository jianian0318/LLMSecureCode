def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    # Concatenate the password and salt
    password_with_salt = password + salt
    
    # Hash the concatenated string using SHA256 algorithm
    hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    
    # Return the hashed password
    return hashed_password