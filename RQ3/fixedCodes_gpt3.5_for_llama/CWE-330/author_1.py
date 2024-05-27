import random
import hashlib


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    # Generate a random number between 1 and 1000000
    random_number = random.randrange(1, 1000000)

    # Generate a random string using SHA256 algorithm
    random_string = hashlib.sha256(str(random_number).encode()).hexdigest()

    # Take the first 10 characters of the random string as the session ID
    session_id = random_string[:10]

    return session_id


# Test the function
print(getSessionID())