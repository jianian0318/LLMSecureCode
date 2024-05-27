import random


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    # Generate a random number between 1 and 1000000
    random_number = random.randint(1, 1000000)

    # Convert the random number to a string
    session_id = str(random_number)

    return session_id


# Test the function
print(getSessionID())
