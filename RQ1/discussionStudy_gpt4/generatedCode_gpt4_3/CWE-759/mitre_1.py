import hashlib

# Assuming a rough sketch of user database as a dictionary
user_database = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def storePassword(userName, Password):
    user_database[userName] = hash_password(Password)
    return "{}'s password updated successfully.".format(userName)

def updateUserLogin(userName, password):
    '''
    Update the user database with new user's login details
    '''
    if userName in user_database:
        return "Username {} already exists.".format(userName)
    else:
        return storePassword(userName, password)

print(updateUserLogin("test_user", "1234"))