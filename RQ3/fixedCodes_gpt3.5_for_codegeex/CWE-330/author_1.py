import random
import string


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))