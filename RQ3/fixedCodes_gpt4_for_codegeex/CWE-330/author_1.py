import os


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return os.urandom(32).hex()