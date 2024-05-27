import random


def getSessionID():
    '''
    Return a random and unique session ID.
    '''
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32))