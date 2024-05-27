import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_password_hash(password: str, salt: str = None):
    '''
    Return a hash of the password using bcrypt.
    '''
    # Generate a salt if it is not provided
    if not salt:
        salt = bcrypt.gensalt()
    else:
        salt = salt.encode()
    
    # Hash the password with the provided salt using bcrypt
    password_hash = bcrypt.hashpw(password.encode(), salt)

    # Return the hashed password and the salt used
    return password_hash, salt

# Example usage:
# Fetch the password from an environment variable instead of hardcoding it
# The environment variable PASSWORD should be set in a .env file or by other means
password_from_env = os.getenv('PASSWORD')
if not password_from_env:
    raise ValueError("The PASSWORD environment variable is not set.")
hashed_password, used_salt = get_password_hash(password_from_env, "")
print(hashed_password, used_salt)