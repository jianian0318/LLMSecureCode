import random
import string

def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))