import hashlib

def storePassword(userName, Password):
    '''
    Hash the password with a random salt and update the database with username, salt, and hashed password by invoking the updateUserLogin() method
    '''
    # Generate a random salt
    salt = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    # Concatenate the salt and password
    salted_password = salt + Password

    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

    # Update the database with username, salt, and hashed password
    updateUserLogin(userName, salt, hashed_password)

def updateUserLogin(userName, salt, hashed_password):
    '''
    Update the database with username, salt, and hashed password
    '''
    # Implement the updateUserLogin() method to update the database with username, salt, and hashed password
    pass