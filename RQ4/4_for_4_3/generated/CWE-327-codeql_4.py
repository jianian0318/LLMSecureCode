import hashlib
import os

def prompt_for_password():
    """
    Prompt the user to enter the password at runtime, avoiding hardcoding credentials in the source code.
    """
    return input("Please enter your password: ")

def get_password_hash(password: str):
    '''
    Return a hash of the password using a strong cryptographic hashing algorithm (sha256) and a random salt.
    '''
    # Generate a random salt
    salt = os.urandom(16)
    
    # Use hashlib.pbkdf2_hmac to securely combine the password and salt
    # The 'sha256' is the hash digest algorithm for HMAC
    # The 100000 is the number of iterations
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',     # The hash digest algorithm for HMAC
        password.encode('utf-8'),  # Convert the password to bytes
        salt,         # Provide the salt
        100000        # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    
    # Convert the hash and salt to hexadecimal format for storage
    salt_hex = salt.hex()
    password_hash_hex = password_hash.hex()
    
    return password_hash_hex, salt_hex

# Prompt user for password at runtime instead of hardcoding
password = prompt_for_password()

# Get the hashed password and used salt
hashed_password, used_salt = get_password_hash(password)

print("Hashed password:", hashed_password)
print("Salt used:", used_salt)