import bcrypt
import getpass

def get_password_hash(password: str, salt: str):
    '''
    Return a bcrypt hash of the password and salt.
    '''
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    
    # Generate a salt specific for bcrypt if not provided, else use the salt provided after converting it to bcrypt salt
    bcrypt_salt = bcrypt.gensalt() if salt == '' else bcrypt.gensalt(rounds=12, prefix=b"2b", salt=salt_bytes)
    
    # Create a hash with bcrypt
    hash_value = bcrypt.hashpw(password_bytes, bcrypt_salt)
    
    # Convert the hash to a string to store in the database
    hash_str = hash_value.decode('utf-8')
    
    return hash_str

# Example usage, prompting user for password and salt
password = getpass.getpass("Enter password: ")
salt = getpass.getpass("Enter salt: ")
password_hash = get_password_hash(password, salt)
print(f"The hashed password is: {password_hash}")