import hashlib
import os

def generate_salt(length=16):
    '''
    Generate a random salt of specified length using os.urandom.
    '''
    return os.urandom(length).hex()

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

# Generate a unique salt
salt = generate_salt()

# Password input prompt to not hardcode credentials
password = input("Enter your password: ")

hashed_password = get_password_hash(password, salt)
print("Hashed Password:", hashed_password)