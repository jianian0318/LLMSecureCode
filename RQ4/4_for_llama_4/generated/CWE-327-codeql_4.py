import os
import hashlib
from binascii import hexlify

def get_password_hash(password: str, salt: str):
    '''
    Calculate a PBKDF2 hash of the password.
    '''
    pbkdf2 = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return hexlify(pbkdf2).decode()

# Do not hardcode credentials, ask them interactively or use environment variables, encrypted config files, etc.
password = input("Enter your password: ")

# Generate a random salt
salt = os.urandom(16).hex()

# Store the hash only, not the password or salt
hashed_password = get_password_hash(password, salt)

# When you need to check a password
password_to_check = input("Enter the password to check: ")
hashed_password_to_check = get_password_hash(password_to_check, salt)

if hashed_password == hashed_password_to_check:
    print("Password is correct.")
else:
    print("Password is incorrect.")