import random
import uuid

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    # Generate a random UUID
    session_id = str(uuid.uuid4())

    return session_id

# Test the function
print(getSessionID())