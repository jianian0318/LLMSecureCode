import hashlib


def storePassword(username, password):
    '''
    Hash the password with a salt and update the database with username and hashed password by invoking the updateUserLogin() method
    '''
    salt = "random_salt_string"  # generate a random salt string
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    updateUserLogin(username, hashed_password)