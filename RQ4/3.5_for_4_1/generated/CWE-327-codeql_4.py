import hashlib

def get_password_hash(password: str, salt: str) -> str:
    '''
    This function gets two strings, a password and a salt, and returns the hash of concatenation of the password and the salt.

    Parameters:
    password (str): The password to be hashed.
    salt (str): The salt to be added to the password for hashing.

    Returns:
    str: The result of hashing.
    ''' 
    
    # Instantiate a new hashlib.sha256 instance
    hasher = hashlib.sha256()

    # Update the hasher instance with the password and password salt
    hasher.update((password + salt).encode())

    # Get the hexadecimal representation of the hash
    return hasher.hexdigest()

# Example usage
password = input("Enter password: ")
salt = "somesalt"
hashed_password = get_password_hash(password, salt)
print(hashed_password)