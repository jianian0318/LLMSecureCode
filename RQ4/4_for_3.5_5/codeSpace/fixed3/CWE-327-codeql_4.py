import hashlib

def get_password_hash(password: str, salt: str) -> str:
    '''
    Return a hash of the password combined with a salt using a stronger cryptographic hash function.
    '''
    # Concatenate the password and salt
    password_salt = password + salt
    
    # Generate the hash using SHA3-512 algorithm
    hash_object = hashlib.sha3_512(password_salt.encode())
    
    # Get the hexadecimal representation of the hash
    password_hash = hash_object.hexdigest()
    
    # Return the hash
    return password_hash

# Example Usage
password = "Secure_Password123"
salt = "Unique_Salt456"

hashed_password = get_password_hash(password, salt)
print("Hashed Password:", hashed_password)