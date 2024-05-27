import hashlib
import os

def get_password_hash(password: str, salt: str):
    '''
    Return a hash of the password and salt.
    '''
    encoded_password = password.encode('utf-8')
    encoded_salt = salt.encode('utf-8')
    iterations = 100000  # Number of iterations for PBKDF2 algorithm
    hash_algorithm = hashlib.sha256  # Hash function (e.g. sha256)
    
    # Generate a random salt if none is provided
    if not salt:
        salt = os.urandom(32)

    # Generate the hash using pbkdf2_hmac method
    password_hash = hashlib.pbkdf2_hmac(hash_algorithm, encoded_password, encoded_salt, iterations)

    return password_hash.hex()

# Example usage
password = input("Enter your password: ")
salt = "random_salt"
hash = get_password_hash(password, salt)
print(hash)