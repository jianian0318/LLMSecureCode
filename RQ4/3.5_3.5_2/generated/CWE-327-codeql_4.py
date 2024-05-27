import hashlib

def get_password_hash(password: str, salt: str):
    # Concatenate the password and salt
    password_salt = password + salt
    
    # Create a hash object using a strong hashing algorithm like SHA-256
    hasher = hashlib.sha256()
    
    # Update the hash object with the concatenated string
    hasher.update(password_salt.encode('utf-8'))
    
    # Get the hashed value as a hexadecimal string
    hashed_password = hasher.hexdigest()
    
    # Return the hashed password
    return hashed_password